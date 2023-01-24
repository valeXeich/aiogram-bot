from aiogram import types, Dispatcher
from bot import bot
from service.users import create_user
from sqlalchemy.ext.asyncio import AsyncSession
from db.base import session


async def command_start(message: types.Message, session: AsyncSession = session):
    await create_user(message, session)
    await bot.send_message(message.from_user.id, 'hi')


def register_handlers_users(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    