# main.py
import nest_asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from handlers import (
    start_command,
    main_menu_command,
    filling_command,
    snickers_filling_command,
    vanilla_filling_command,
    honey_filling_command,
    examples_command,
    order_command,
    process_filling,
    process_wishes,
    process_full_name,
    process_product,
    process_design_photo,
    process_design_text,
    process_delivery_type,
    process_weight,
    process_phone_number,
    ai_command,
    process_description_ai,
)
from states import OrderState, Form


nest_asyncio.apply()

# Инициализация бота
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Регистрация обработчиков
dp.register_message_handler(lambda message, state: start_command(message, state, bot),
                            commands=['start'], state='*',
                            run_task=True)

dp.register_message_handler(lambda message, state: main_menu_command(message, state, bot),
                            text='Главное меню', state='*',
                            run_task=True)

dp.register_message_handler(lambda message: filling_command(message, bot), text='Начинка',
                            run_task=True)

dp.register_message_handler(lambda message: snickers_filling_command(message, bot), text='Сникерс',
                            run_task=True)

dp.register_message_handler(lambda message: vanilla_filling_command(message, bot), text='Ваниль',
                            run_task=True)

dp.register_message_handler(lambda message: honey_filling_command(message, bot), text='Мед',
                            run_task=True)

dp.register_message_handler(lambda message: examples_command(message, bot), text='Примеры работ',
                            run_task=True)

dp.register_message_handler(lambda message, state: order_command(message, state, bot), text='Заявка',
                            run_task=True)

dp.register_message_handler(lambda message, state: process_filling(message, state, bot),
                            state=OrderState.filling, run_task=True)

dp.register_message_handler(lambda message, state: process_wishes(message, state, bot),
                            state=OrderState.wishes, run_task=True)

dp.register_message_handler(lambda message, state: process_full_name(message, state, bot),
                            state=OrderState.full_name, run_task=True)

dp.register_message_handler(lambda message, state: process_weight(message, state, bot),
                            state=OrderState.date_time, run_task=True)

dp.register_message_handler(lambda message, state: process_product(message, state, bot),
                            state=OrderState.product, run_task=True)

dp.register_message_handler(lambda message, state: process_design_photo(message, state, bot),
                            content_types=types.ContentType.PHOTO,
                            state=OrderState.design, run_task=True)

dp.register_message_handler(lambda message, state: process_design_text(message, state, bot),
                            state=OrderState.design, run_task=True)

dp.register_message_handler(lambda message, state: process_delivery_type(message, state, bot),
                            state=OrderState.delivery_type,
                            run_task=True)

dp.register_message_handler(lambda message, state: process_phone_number(message, state, bot),
                            state=OrderState.phone_number,
                            run_task=True)

dp.register_message_handler(lambda message, state: ai_command(message, state, bot),
                            text='ИИ-генерация', state="*", run_task=True)

dp.register_message_handler(lambda message, state: process_description_ai(message, state, bot),
                            state=Form.description,
                            run_task=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
