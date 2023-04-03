from aiogram import types, Dispatcher
from random import choice
from config import bot
from .loader import download_video

async def game(message: types.Message):
    if message.text.startswith('.'):
        await message.pin()

    if message.text == "game":
        list1 = [ '⚽️', '🏀', '🎲', '🎰', '🎯', '🎳']
        emoji = choice(list1)
        await bot.send_message(message.chat.id,text=emoji)

async def video_download(message: types.Message):
    if "youtube.com" in message.text:
        await message.answer("Загрузка...")
        video = open(f"../{download_video(message.text)}", "rb")
        await message.answer_audio(video)
        await message.answer("Не благодари")



def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])
    dp.register_message_handler(video_download, content_types=['text'])
