from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


Token = config('Token')

storage = MemoryStorage()
bot = Bot(Token)
dp = Dispatcher(bot=bot, storage=storage)

ADMINS = (1045935241,)
