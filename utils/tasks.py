import asyncio

from bot import bot
from service.users import get_users
from db.base import session


async def scheduled_task():
    counter = 0
    while True:
        try:
            users = await get_users(session)
            current_user = users[counter]
            bot.send_message(current_user.tg_user_id, "I'ts schedule message")
            counter += 1
            if counter == 1000:
                await asyncio.sleep(300)
        except asyncio.CancelledError:
            break
        except IndexError:
            break