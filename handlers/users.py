from aiogram import types, Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession

from bot import bot
from service.users import create_user_or_group
from db.base import session


async def command_start(message: types.Message, session: AsyncSession = session):
    created = await create_user_or_group(message, session)
    is_group = message.chat.type in ["group", "supergroup"]
    if is_group and not created:
        await bot.send_message(message.chat.id, 'Group already added to the DB')
    elif is_group and created:
        await bot.send_message(message.chat.id, 'Group added successfully to the DB')
    if message.chat.type == "private" and not created:
        await bot.send_message(message.from_user.id, 'You are already added to the DB')
    else:
        await bot.send_message(message.from_user.id, 'You are added successfully to the DB')


def register_handlers_users(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    