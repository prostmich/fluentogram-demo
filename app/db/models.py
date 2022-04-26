from sqlalchemy import Column, BigInteger, String

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    lang = Column(String(2), default="ru")
