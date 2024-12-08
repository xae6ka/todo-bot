import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers.handlers import command_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(command_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())