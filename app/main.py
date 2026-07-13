import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is missing")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Hello! I'm Anaya AI ❤️\n\nBot is working successfully."
    )


@dp.message()
async def echo(message: Message):
    await message.answer(
        f"You said:\n\n{message.text}"
    )


async def main():
    print("Anaya AI Started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())