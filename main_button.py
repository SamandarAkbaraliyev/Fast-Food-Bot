from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱Telefon raqamni ulashish📱", request_contact=True)
        ],
        [
            KeyboardButton(text="🗺 LOKATSIYANI ULASHISH 🗺", request_location=True)
        ],
        [
            KeyboardButton(text="🍽 MENU 🍽")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
