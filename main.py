import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def forward_all(message: Message):
    try:
        await bot.forward_message(
            chat_id=GROUP_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )
    except Exception as e:
        print("Ошибка:", e)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())