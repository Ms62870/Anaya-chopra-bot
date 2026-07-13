import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
            "👋 Hello! I'm Anaya AI.\n\n"
                    "I'm your AI companion. ❤️"
                        )

                        async def main():
                            await dp.start_polling(bot)

                            if __name__ == "__main__":
                                asyncio.run(main())
                            