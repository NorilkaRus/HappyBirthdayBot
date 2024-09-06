import os
import asyncio
import logging

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandStart
from app.handlers import router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

load_dotenv('.env')

TOKEN_API = os.getenv('TOKEN_API')

bot = Bot(token=TOKEN_API, default=DefaultBotProperties(parse_mode=ParseMode.HTML,))
dp = Dispatcher()



# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
    except RuntimeError:
        print('Exit')
