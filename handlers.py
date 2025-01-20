from aiogram import types
from aiogram.dispatcher import FSMContext
from config import ADMIN_ID
from keyboards import start_kb, main_menu_kb, filling_kb
from states import OrderState, Form
from text2image import Text2ImageAPI, display_image
from config import FUSION_BRAIN_URL, FUSION_BRAIN_API_KEY, FUSION_BRAIN_SECRET_KEY
from aiogram import Bot


async def start_command(message: types.Message, state: FSMContext, bot: Bot):
    await state.finish()
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Стартовое меню',
        parse_mode='HTML',
        reply_markup=start_kb,
    )


async def main_menu_command(message: types.Message, state: FSMContext, bot: Bot):
    await state.finish()
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Стартовое меню',
        parse_mode='HTML',
        reply_markup=start_kb,
    )


async def filling_command(message: types.Message, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='\n•Милка- шоколадные коржи, мусс на белом шоколаде, ганаш на молочном шоколаде \
        \n•Дон Панчо- шоколадный бисквит в прослойке с вишней \
        \n•Шоколадный бархат - шоколадные коржи с кремом на основе взбитых сливок и шоколада \
        \n•Сникерс - шоколадные коржи, со сливочной карамелью, жареным арахисом и шоколадным муссом \
        \n•Рафаэлло - ванильный бисквит с жареным миндалем кокосом крем на основе маскарпоне \
        \n•Медовый с карамелью - тонкие медовые коржи с карамельно-сливочным кремом \
        \n•Медовый с ягодной начинкой - тонкие медовые коржи'
             ' со сливочным кремом и ягодным конфи в прослойке \
        \n•Наполеон - слоеные коржи с кремом Димлопант(напоминает вкус мороженого пломбир) \
        \n•Малина фисташка- ванильный бисквит, крем с пастой фисташки, малиновое конфи \
        \n•Красный бархат - воздушные коржи с добавлением какао с кремом чиз на основе'
             ' маскорпоне (+в прослойку можно добавить ягодное конфи) \
        \n•Клубника банан - воздушные ванильные коржи с кремом из'
             ' взбитых сливок с клубникой и бананом в прослойке \
        \n•Брюс - шоколадные коржи, взбитый шоколадный ганаш,'
             ' соленая карамель, хрустящие шарики криспи \
        \n•Молочная девочка - тонкие коржи сгущеном молоке, крем на основе маскарпоне и взбитых'
             ' сливок, в прослойку можно добавить клубнику, малину или персик \
        \n•Вишня в шоколаде - шоколадные коржи, шоколадный ганаш,'
             ' вишнёвое конфи с цельными ягодами вишни \
          •Ягода Малина - ванильный бисквит, мусс на основе ягодного йогурта,'
             ' малиновое конфи, малиновый мусс в прослойках',
        reply_markup=filling_kb,
        parse_mode='HTML',
    )


async def snickers_filling_command(message: types.Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text='Текст Сникерс', reply_markup=main_menu_kb,
                           parse_mode='HTML')


async def vanilla_filling_command(message: types.Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text='Текст Ваниль', reply_markup=main_menu_kb,
                           parse_mode='HTML')


async def honey_filling_command(message: types.Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text='Текст Мед', reply_markup=main_menu_kb,
                           parse_mode='HTML')


async def examples_command(message: types.Message, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='С примерами работ можете ознакомиться по ссылке\n'
             'https://drive.google.com/drive/folders/13ffeYfrRBZ8hEzt3FeYwDAxo-lLHJUUa',
        reply_markup=start_kb,
        parse_mode='HTML',
    )


async def order_command(message: types.Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Какая нужна начинка?', reply_markup=main_menu_kb, parse_mode='HTML')
    await state.set_state(OrderState.filling)


async def process_filling(message: types.Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Укажите пожелания', reply_markup=main_menu_kb, parse_mode='HTML')
    await state.update_data(filling=message.text)
    await state.set_state(OrderState.wishes)


async def process_wishes(message: types.Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Введите ваше ФИО', reply_markup=main_menu_kb, parse_mode='HTML')
    await state.update_data(wishes=message.text)
    await state.set_state(OrderState.full_name)


async def process_full_name(message: types.Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Дата и время, когда нужен торт', reply_markup=main_menu_kb,
        parse_mode='HTML')
    await state.update_data(full_name=message.text)
    await state.set_state(OrderState.date_time)


async def process_weight(message: types.Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Вес?', reply_markup=main_menu_kb, parse_mode='HTML')
    await state.update_data(date_time=message.text)
    await state.set_state(OrderState.product)


async def process_product(message: types.Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Какой дизайн?\nПришлите фото или напишите текстом',
        reply_markup=main_menu_kb,
        parse_mode='HTML',
    )
    await state.update_data(product=message.text)
    await state.set_state(OrderState.design)


async def process_design_photo(message: types.Message, state: FSMContext, bot: Bot):
    file_id = message.photo[0].file_id
    await state.update_data(design_type='photo', design=file_id)
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Доставка или самовывоз?\nЕсли доставка, оставьте еще в новой строке адрес и время',
        reply_markup=main_menu_kb,
    )
    await state.set_state(OrderState.delivery_type)


async def process_design_text(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(design_type='text', design=message.text)
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Доставка или самовывоз?\nЕсли доставка, оставьте в строке адрес и время',
        reply_markup=main_menu_kb,
    )
    await state.set_state(OrderState.delivery_type)


async def process_delivery_type(message: types.Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id, text='Оставьте свой номер телефона', reply_markup=main_menu_kb
    )
    await state.update_data(delivery_type=message.text)
    await state.set_state(OrderState.phone_number)


async def process_phone_number(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(phone_number=message.text)
    data = await state.get_data()
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text='Ваша заявка была отправлена',
                           reply_markup=main_menu_kb)
    if data['design_type'] == 'photo':
        await bot.send_photo(
            chat_id=ADMIN_ID,
            photo=data['design'],
            caption=f'Новая заявка\nНачинка {data["filling"]}\nПожелания {data["wishes"]}'
                    f'\nФИО {data["full_name"]}\nДата-время {data["date_time"]}'
                    f'\nИзделие {data["product"]}'
                    f'\nТип доставки {data["delivery_type"]}\nНомер телефона {data["phone_number"]}\n',
        )
    else:
        await bot.send_message(
            chat_id=ADMIN_ID,
            text=f'Новая заявка\nНачинка {data["filling"]}\nПожелания {data["wishes"]}'
                 f'\nФИО {data["full_name"]}\nДата-время {data["date_time"]}'
                 f'\nИзделие {data["product"]}\nДизайн {data["design"]}'
                 f'\nТип доставки {data["delivery_type"]}\nНомер телефона {data["phone_number"]}\n',
        )


async def ai_command(message: types.Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        chat_id=message.from_user.id, text='Опишите изделие', reply_markup=filling_kb, parse_mode='HTML'
    )
    await state.set_state(Form.description)


async def process_description_ai(message: types.Message, state: FSMContext, bot: Bot):
    description = message.text
    api = Text2ImageAPI(FUSION_BRAIN_URL, FUSION_BRAIN_API_KEY, FUSION_BRAIN_SECRET_KEY)
    try:
        model_id = api.get_model()
        uuid = api.generate(description, model_id)
        images = api.check_generation(uuid)
        for index, image_data in enumerate(images):
            temp_file = display_image(image_data)
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=temp_file,
                caption=f"Сгенерированное изображение {index + 1}"
            )
        await state.finish()
    except Exception as e:
        await bot.send_message(
            chat_id=message.from_user.id, text=f"Ошибка: {e}"
        )
        await state.finish()
