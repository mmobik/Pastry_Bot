# text2image.py
import base64
import json
import time
from io import BytesIO
import requests
from PIL import Image


class Text2ImageAPI:
    """Преобразует текст в изображение"""

    def __init__(self, url, api_key, secret_key):  # Инициализируем апи
        self.url = url
        self.auth_headers = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self) -> str:  # Получаем айди модели
        response = requests.get(self.url + 'key/api/v1/models', headers=self.auth_headers)
        response.raise_for_status()
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024) -> str:  # Генерация изображения
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {"query": prompt},
        }
        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json'),
        }
        response = requests.post(
            self.url + 'key/api/v1/text2image/run', headers=self.auth_headers, files=data
        )
        response.raise_for_status()
        data = response.json()
        return data.get('uuid')

    def check_generation(self, request_id, attempts=10, delay=10) -> list:
        #  Проверяет статус генерации и возвращает сгенерированные изображения.
        while attempts > 0:
            response = requests.get(
                self.url + 'key/api/v1/text2image/status/' + request_id, headers=self.auth_headers
            )
            response.raise_for_status()
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']
            if data['status'] in ['INITIAL', 'PROCESSING']:
                time.sleep(delay)
            attempts -= 1
        raise Exception("Время генерации истекло")


def display_image(image_data):  # Декодирует base64 строку в изображение.
    image_bytes = base64.b64decode(image_data)
    image = Image.open(BytesIO(image_bytes))
    temp_file = BytesIO()
    image.save(temp_file, format='PNG')
    temp_file.seek(0)
    return temp_file
