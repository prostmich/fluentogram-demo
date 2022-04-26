from aiogram.dispatcher.filters.callback_data import CallbackData


class LangCallbackData(CallbackData, prefix="lang"):
    lang_code: str
