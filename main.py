import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import config
from handlers import join_requests_router, welcome_router

async def main():
    logging.basicConfig(level=logging.INFO)
    
    # Инициализируем бота и диспетчер
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()
    
    # Регистрируем роутеры
    dp.include_router(welcome_router)
    dp.include_router(join_requests_router)
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
