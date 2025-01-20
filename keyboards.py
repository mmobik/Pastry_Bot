# keyboards.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Стартовая клавиатура
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_kb.add(
    KeyboardButton(text='Начинка'),
    KeyboardButton(text='Заявка'),
    KeyboardButton(text='Примеры работ'),
    KeyboardButton(text='ИИ-генерация'),
)

# Клавиатура главного меню
main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_menu_kb.add(KeyboardButton(text='Главное меню'))

# Клавиатура выбора начинки
filling_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
filling_kb.add(
    KeyboardButton(text='Главное меню'),
)
