from aiogram import Router


def get_router():
    from .private import private_router

    router = Router()
    router.include_router(private_router)
    return router
