import os
from dotenv import load_dotenv, dotenv_values

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import logging

# Load variables from the .env file
load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Привет. \nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}")

@dp.message(Command("help"))
async def get_help(message: Message):
    await message.answer("Это команда /help")

@dp.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.answer("OK!")

@dp.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAMTaUNGaO90LvuopgcM75C6F2FLTswAAhYUaxuF6hlKmq6KHxgqs6QBAAMCAAN5AAM2BA",
                               caption="Единорог")

@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())