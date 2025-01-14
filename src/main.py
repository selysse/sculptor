import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message

API_TOKEN = ""

dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("Hello")

async def run() -> None:
    """
    
    """
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(run())