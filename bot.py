import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = "9137635106:AAHyiCxAFTKxnWi0B6LgvN2LLQsJJdE4DOQ"
WEBAPP_URL = "https://noom123412.github.io/shopchik/"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

WELCOME = (
    "🖤 <b>The Grand</b>\n\n"
    "Подписки на SoundCloud, Spotify, Claude, ChatGPT и Telegram Premium.\n"
    "Тихо, надёжно, по делу.\n\n"
    "Нажмите кнопку ниже, чтобы открыть магазин."
)

def main_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="🛍 Открыть магазин", web_app=WebAppInfo(url=WEBAPP_URL))
    kb.button(text="ℹ️ О магазине", callback_data="about")
    kb.adjust(1)
    return kb.as_markup()

@dp.message(CommandStart())
async def start(m: Message):
    await m.answer(WELCOME, reply_markup=main_kb(), parse_mode="HTML")

@dp.callback_query(F.data == "about")
async def about(cb: CallbackQuery):
    await cb.message.answer(
        "The Grand — магазин цифровых подписок.\n"
        "Работаем с 2022 года. Гарантия на весь срок подписки.\n"
        "Поддержка отвечает в течение 15 минут."
    )
    await cb.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
