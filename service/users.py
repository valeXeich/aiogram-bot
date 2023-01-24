from db.models import User

from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def create_user(message: Message, session: AsyncSession):
    check = await check_user(message, session)
    if check:
        return
    username = message.from_user.username
    tg_user_id = message.from_user.id
    user = User(username=username, tg_user_id=tg_user_id)
    session.add(user)
    await session.commit()


async def get_user(message: Message, session: AsyncSession):
    username = message.from_user.username
    query = select(User).where(User.username == username)
    result = await session.execute(query)
    return result.scalars().first()


async def get_users(session: AsyncSession):
    query = select(User)
    result = await session.execute(query)
    return result.scalars().all()


async def check_user(message: Message, session: AsyncSession):
    user = await get_user(message, session)
    if user:
        return True
    return