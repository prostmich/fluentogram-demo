from aiogram import Router, F
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, User
from fluentogram import TranslatorRunner, TranslatorHub

from app.db.repo import Repo
from app.utils.callback_data import LangCallbackData
from app.utils.generators import get_start_inline_keyboard, get_lang_select_keyboard

private_router = Router()
private_router.message.filter(F.chat.type == "private")
private_router.callback_query.filter(F.message.chat.type == "private")


@private_router.message(Command(commands="start"))
async def cmd_start(message: Message, i18n: TranslatorRunner, event_from_user: User):
    text = i18n.welcome(user=event_from_user.full_name)
    markup = get_start_inline_keyboard(i18n)
    await message.answer(text=text, reply_markup=markup)


@private_router.callback_query(F.data == "change_lang")
async def cb_change_lang(query: CallbackQuery, i18n: TranslatorRunner):
    await query.answer()
    text = i18n.change.lang.menu()
    await query.message.edit_text(text=text, reply_markup=get_lang_select_keyboard())


@private_router.callback_query(LangCallbackData.filter())
async def cb_change_lang(
    query: CallbackQuery,
    i18n_hub: TranslatorHub,
    callback_data: LangCallbackData,
    repo: Repo,
):
    i18n = i18n_hub.get_translator_by_locale(callback_data.lang_code)
    await query.answer(i18n.change.lang.success())
    await repo.change_user_lang(query.from_user.id, callback_data.lang_code)
    await query.message.delete()
    await cmd_start(query.message, i18n, query.from_user)
