import asyncio

from aiogram.utils import executor

from bot import dp
from handlers import users
from utils.db import init_models
from utils.tasks import scheduled_task


async def on_startup(_):
    await init_models()
    task = asyncio.create_task(scheduled_task())
    try:
        await task
    except asyncio.CancelledError:
        task.cancel()
    print('Bot online')


users.register_handlers_users(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    