from sqlalchemy import Column, Integer, String

from database import Base


class DBMessage(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    bot_token = Column(String(200), nullable=False)
    chat_id = Column(String(200), nullable=False)
    text = Column(String(500), nullable=False)
