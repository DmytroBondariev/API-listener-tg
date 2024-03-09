from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from api_listener import models, schemas


async def get_all_messages(db: AsyncSession):
    query = select(models.DBMessage)
    message_list = await db.execute(query)
    return [message[0] for message in message_list.fetchall()]


async def create_message(db: AsyncSession, message: schemas.MessageCreate):
    query = insert(models.DBMessage).values(text=message.text, chat_id=message.chat_id, bot_token=message.bot_token)

    result = await db.execute(query)
    await db.commit()
    response = {**message.model_dump(), "id": result.lastrowid}
    return response
