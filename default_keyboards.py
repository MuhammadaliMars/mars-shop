from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="mars bozori"),
            KeyboardButton(text="qoshish"),
        ],
        [
           KeyboardButton(text="sotish"),
           KeyboardButton(text="profil"), 
        ]
    ], resize_keyboard=True
)