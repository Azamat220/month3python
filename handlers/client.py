from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from keyboards.client_kb import start_markup
from data_base.bot_dp import sql_command_random
from . import news


async def start_command(message: types.Message):
    await message.answer("Hello world!", reply_markup=start_markup)



async def help_command(message: types.Message):
    photo = open('image/img.png', 'rb')
    await message.answer_photo(photo=photo,
                               caption="Сам разбирайся!")



async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "By whom invented Python?"
    answer = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


async def get_random_user(message: types.Message):
    random_user = await sql_command_random()
    await message.answer_photo(
        photo=random_user[-1],
        caption=f"{random_user[1]} {random_user[2]} {random_user[3]} {random_user[4]}\n"
                f"@{random_user[5]}"
    )


async def get_news(message: types.Message):
    news_list = news.parser()
    for i in news_list:
        await message.answer(
            f"{i['link']}\n\n"
            f"<b><a href='{i['link']}'>{i['title']}</a></b>\n"
            f"{i['description']}\n"
            f"{i['date_from_html']}\n",
            # parse_mode=ParseMode.HTML
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(get_news, commands=['news'])