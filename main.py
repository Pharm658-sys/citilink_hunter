import asyncio
from citilink_hunter.config import settings
from citilink_hunter.handlers import user
from aiogram import Bot, Dispatcher

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()

dp.include_router(user.user_router)

async def main():
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())
