import asyncio

from bot import dp
from handlers import users

from utils.db import init_models


async def on_startup(_):
    print('Bot online')

async def main():
    await init_models()
    await dp.start_polling()
    await on_startup()

users.register_handlers_users(dp)

if __name__ == '__main__':
    asyncio.run(main())
    