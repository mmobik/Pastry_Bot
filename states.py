# states.py
from aiogram.dispatcher.filters.state import State, StatesGroup


class OrderState(StatesGroup):
    """Состояния для обработки заказа."""
    filling = State()  # Выбор начинки
    wishes = State()  # Пожелания
    full_name = State()  # Полное ФИО
    date_time = State()  # Примерная дата
    design = State()  # Дизайн
    product = State() # Вес
    delivery_type = State()  # Тип доставки
    phone_number = State()  # Номер телефона


class Form(StatesGroup):
    """Состояние для ожидания описания изделия для генерации изображения."""
    description = State()
