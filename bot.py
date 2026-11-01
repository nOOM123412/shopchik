
import asyncio, os
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton,
    WebAppInfo,
)
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

WELCOME = (
    "🖤 <b>SubShop</b>\n\n"
    "Подписки на SoundCloud, Spotify, Claude, ChatGPT и Telegram + Premium.\n"
    "Аккуратно, быстро, без лишнего.\n\n"
    "Нажмите кнопку ниже, чтобы открыть магазин."
)

def main_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="🛍 Открыть магазин", web_app=WebAppInfo(url=WEBAPP_URL))
    kb.button(text="ℹ️ О сервисе", callback_data="about")
    kb.adjust(1)
    return kb.as_markup()

@dp.message(CommandStart())
async def start(m: Message):
    await m.answer(WELCOME, reply_markup=main_kb(), parse_mode="HTML")

@dp.callback_query(F.data == "about")
async def about(cb: CallbackQuery):
    await cb.message.answer(
        "SubShop — магазин подписок.\n"
        "Оплата через Telegram Stars / крипту / карту (настраивается на бэкенде).\n"
        "После оплаты доступ выдаётся автоматически."
    )
    await cb.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
