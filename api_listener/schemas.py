from pydantic import BaseModel


class MessageCreate(BaseModel):
    text: str
    chat_id: str
    bot_token: str


class Message(BaseModel):
    id: int
    text: str
    chat_id: str
    bot_token: str
