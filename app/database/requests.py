from app.datebase.models import async_session
from app.database.models import User, Category, Item
from sqlalchemy import select

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar()