import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from google import genai

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

client = genai.Client(api_key=GEMINI_API_KEY)


@dp.message(CommandStart())
async def start(message: Message):
    models = []

    try:
        for model in client.models.list():
            models.append(model.name)

        await message.answer("\n".join(models[:20]))

    except Exception as e:
        await message.answer(str(e))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())