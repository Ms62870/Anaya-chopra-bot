import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from google import genai

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

client = genai.Client(api_key=GEMINI_API_KEY)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
            "👋 Hi, I'm Anaya AI ❤️\n\nI'm happy to chat with you."
                )

                @dp.message()
                async def chat(message: Message):
                    try:
                            response = client.models.generate_content(
                                        model="gemini-2.5-flash",
                                                    contents=message.text,
                                                            )
                                                                    await message.answer(response.text)
                                                                        except Exception:
                                                                                await message.answer("⚠️ Sorry, I'm having trouble right now.")

                                                                                async def main():
                                                                                    await dp.start_polling(bot)

                                                                                    if __name__ == "__main__":
                                                                                        asyncio.run(main())