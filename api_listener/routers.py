from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.chat_action import logger
from aiogram.utils.token import TokenValidationError
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api_listener import schemas, crud
from dependencies import get_db_session

router = APIRouter()


@router.post("/")
async def create_message(message: schemas.MessageCreate, db: AsyncSession = Depends(get_db_session)):
    message = await crud.create_message(db=db, message=message)
    try:
        bot = Bot(token=message['bot_token'])
    except TokenValidationError:
        logger.error(f"TokenValidationError: invalid bot token provided")
        raise HTTPException(status_code=400, detail="Invalid bot token provided")
    try:
        await bot.send_message(chat_id=message['chat_id'], text=message['text'])
    except TelegramBadRequest:
        logger.error(f"TelegramBadRequest: invalid chat id provided")
        raise HTTPException(status_code=400, detail="Invalid chat id provided")
    finally:
        await bot.session.close()
    return {200: {"description": "Message sent"}}
