from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = '6145346764:AAHYqBdHhvS8TBR_cXkK0MYBtQfhGDo-AkI'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())