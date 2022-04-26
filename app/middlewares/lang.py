from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery
from fluentogram import TranslatorRunner

from app.db.repo import Repo
from app.services.fluent import FluentService


class LangMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ) -> Any:
        fluent: FluentService = data["fluent"]
        repo: Repo = data["repo"]
        user_lang = (await repo.get_user(event.from_user.id)).lang
        translator_runner: TranslatorRunner = fluent.get_translator_by_locale(user_lang)
        data["i18n"] = translator_runner
        data["i18n_hub"] = fluent.hub
        return await handler(event, data)
