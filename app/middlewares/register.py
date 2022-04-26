from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery

from app.db.repo import Repo


class RegisterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ) -> Any:
        repo: Repo = data["repo"]
        user = await repo.get_user(event.from_user.id)
        if not user:
            await repo.create_user(event.from_user.id)
        return await handler(event, data)
