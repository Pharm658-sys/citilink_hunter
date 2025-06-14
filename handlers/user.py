from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command


from citilink_hunter.parser.runer import main
from citilink_hunter.keyboards.inline import next_page_keyboard


user_router = Router()

@user_router.message(Command("start"))
async def cmd_start(message: Message):
	await message.answer("Привет! Я бот который может спарсить товары с сайта Citilink.ru 💻. Напишите команду /laptops для парсинга.")


@user_router.message(F.text.lower() == "/laptops")
async def cmd_laptops(msg: Message):
	laptops = await main(page_number=1)

	if not laptops:
		await msg.answer("Ноутбуки не найдены.")
		return

	for laptop in laptops:
		text = f"{laptop['title']}\nЦена: {laptop['price']}\nСсылка: {laptop['link']}"
		await msg.answer(text)


	text = ""
	for item in laptops:
		text += f"💻 <b>{item['title']}</b>\n💸 {item['price']}Р\n {item['link']}\n\n"

		await msg.answer(
			text,
			reply_markup=next_page_keyboard("laptops",1,),
			parse_mode="HTML"
		)

@user_router.callback_query(F.data.startswith("next:laptops"))
async def next_laptops_page(call: CallbackQuery):
	await call.answer(cache_time=0)
	_, _, page_str = call.data.split(":")
	page = int(page_str)

	laptops = await main(page)

	if not laptops:
		await call.answer("Больше ноутбуков нет.")


	text = ""
	for item in laptops:
		text += f"💻 <b>{item['title']}</b>\n💸 {item['price']}Р\n🔗 {item['link']}\n\n"

	await call.message.edit_text(
		text,
		reply_markup=next_page_keyboard("laptops", page),
		parse_mode="HTML"
	)


