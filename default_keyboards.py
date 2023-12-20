from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=""),
            KeyboardButton(text=""),
        ],
        [
           KeyboardButton(text=""),
           KeyboardButton(text=""), 
        ]
    ], resize_keyboard=True
)