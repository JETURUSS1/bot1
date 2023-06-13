from aiogram.utils import executor

from bot_create import dp
from handlers.main import register_main_handlers

async def on_startup(_):
    register_main_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

