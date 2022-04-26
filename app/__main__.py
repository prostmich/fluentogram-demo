import asyncio
import logging
from pathlib import Path

from aiogram import Dispatcher, Bot
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config_reader import config
from app.db.base import Base
from app.handlers.setup import get_router
from app.middlewares.setup import setup_middlewares
from app.services.fluent import FluentService, TranslationLoader


async def _configure_postgres():
    engine = create_async_engine(
        config.postgres.url,
        future=True,
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # todo alembic
    return sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


def _configure_fluent():
    locales_map = {
        "ru": ("ru", "en"),
        "en": ("en", "ru"),
    }
    loader = TranslationLoader(
        Path("/resources/locales"),
    )
    return FluentService(loader, locales_map)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()
    session_maker = await _configure_postgres()
    setup_middlewares(dp, session_maker)
    dp.include_router(get_router())
    fluent = _configure_fluent()
    await dp.start_polling(bot, fluent=fluent)


asyncio.run(main())
