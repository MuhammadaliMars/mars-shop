from aiogram import Dispatcher, Bot, types, executor
from default_keyboards import user_main_menu
from aiogram.contrib.fsm_storage.memory import MemoryStorage


token = "6496322618:AAHZ-UFHi4VnUfKNiie05edNvtS_s9Lr83o"

storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "assalomu aleykum"
    await message.answer(text=text, reply_markup=user_main_menu)
    


       


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)