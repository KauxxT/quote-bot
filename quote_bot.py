import asyncio
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = "7979898115:AAE7UGMxfgrUiIOkF9FCSBVVoxgIUXdtDmQE"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Список цитат
quotes = [
    "«Не бойся медленно идти вперёд, бойся стоять на месте.» — Китайская пословица",
    "«Делай или не делай. Не существует 'попробую'.» — Йода",
    "«Я знаю только то, что ничего не знаю.» — Сократ",
    "«Глупец думает, что он мудр, мудрец знает, что он глуп.» — Шекспир",
    "«Если работа мешает жить — бросай работу!»",
    "«Лучше быть последним — но первым в очереди за счастьем.»"
]


def quote_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Следующая цитата")]],
        resize_keyboard=True
    )


@dp.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer("Привет! Жми кнопку и получай цитаты:", reply_markup=quote_keyboard())


@dp.message(F.text == "Следующая цитата")
async def send_quote(message: types.Message):
    quote = random.choice(quotes)
    await message.answer(quote)


@dp.message()
async def fallback(message: types.Message):
    await message.answer("Жми кнопку 'Следующая цитата' или введи /start")

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
