from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker

from .lang import LangMiddleware
from .repo import RepoMiddleware
from .register import RegisterMiddleware


def setup_middlewares(dp: Dispatcher, session_maker: sessionmaker):
    dp.update.outer_middleware.register(RepoMiddleware(session_maker))
    dp.message.outer_middleware.register(RegisterMiddleware())
    dp.callback_query.outer_middleware.register(RegisterMiddleware())
    dp.message.outer_middleware.register(LangMiddleware())
    dp.callback_query.outer_middleware.register(LangMiddleware())
