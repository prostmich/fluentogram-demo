from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from fluentogram import TranslatorRunner

from app.utils.callback_data import LangCallbackData


def get_start_inline_keyboard(i18n: TranslatorRunner) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text=i18n.change.lang.btn(), callback_data="change_lang")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_lang_select_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text="🇺🇸", callback_data=LangCallbackData(lang_code="en").pack()
            ),
            InlineKeyboardButton(
                text="🇷🇺", callback_data=LangCallbackData(lang_code="ru").pack()
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
