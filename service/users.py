from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db.models import User


async def create_user_or_group(message: Message, session: AsyncSession):
    if message.chat.type in ["group", "supergroup"]:
        username = None
        tg_id = message.chat.id
    else:
        username = message.from_user.username
        tg_id = message.from_user.id
    check = await check_user(tg_id, session)
    if check:
        return False
    user = User(username=username, tg_user_id=tg_id)
    session.add(user)
    await session.commit()
    return True


async def get_user(tg_id: int, session: AsyncSession):
    query = select(User).where(User.tg_user_id == tg_id)
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