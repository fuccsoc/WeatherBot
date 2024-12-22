from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

route_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Добавить точку", callback_data="route_add")],
            [InlineKeyboardButton(text="Отправить", callback_data="route_ok")]
        ]
    )

days_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1 день", callback_data="days_1")],
            [InlineKeyboardButton(text="3 дня", callback_data="days_3")],
            [InlineKeyboardButton(text="5 дней", callback_data="days_5")]
        ]
    )
