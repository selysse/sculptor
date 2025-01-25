"""

"""
import logging
import asyncio
import os
from pathlib import Path
from datetime import datetime

from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message


dp = Dispatcher()


@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("Hello")

@dp.message(F.photo)
async def download_image(message: Message, bot: Bot):
    await bot.download(
        message.photo[-1],
        destination=f"./{message.photo[-1].file_id}.jpg"
    )

async def run() -> None:
    """
    Runner bots
    """
    log_name = f'logs/{datetime.now().strftime("%Y-%m-%d")}.log'
    Path(log_name).parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        filename=log_name,
        filemode="a"
    )
    token = os.environ['TELEGRAM_TOKEN']
    bot = Bot(token=token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run())
