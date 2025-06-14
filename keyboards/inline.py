from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def next_page_keyboard(laptops: str, page:  int):
	builder = InlineKeyboardBuilder()
	builder.row(
		InlineKeyboardButton(
			text="Следующая страница",
			callback_data=f"next:{laptops}:{page + 1}"
		)
	)
	return builder.as_markup()

