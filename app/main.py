
import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from google import genai

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL = "models/gemini-flash-latest"


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Hello! I'm Anaya AI ❤️\n\nAsk me anything."
    )


@dp.message()
async def chat(message: Message):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=message.text
        )

        if response.text:
            await message.answer(response.text)
        else:
            await message.answer("⚠️ No response from Gemini.")

    except Exception as e:
        await message.answer(f"❌ Error:\n{e}")
async def main():
    print("🚀 Anaya AI Started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())