import os
from dotenv import load_dotenv, dotenv_values

import asyncio
from aiogram import Bot, Dispatcher

import logging

from app.handlers import router

# Load variables from the .env file
load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())