import asyncio
import logging
from aiogram.types import ChatJoinRequest

from config import TOKEN_API
from aiogram import Bot, Dispatcher
from aiogram.types.input_file import FSInputFile

bot = Bot(TOKEN_API)
dp = Dispatcher()


async def approve_request(chat_join: ChatJoinRequest):
    msg = (
        'Привет 👋 '
    )

    await bot.send_message(chat_id=chat_join.from_user.id, text=msg)
    file = FSInputFile("../10 СОВЕТОВ.pdf")
    await bot.send_document(chat_id=chat_join.from_user.id,
                            document=file)
    await chat_join.approve()


async def main():
    dp.chat_join_request.register(approve_request)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
