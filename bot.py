import os
import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# from config import TOKEN
# Токен получаем здесь https://t.me/BotFather
TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

# Задание
# - Включить запись log в файл
# - Бот принимает кириллицу отдаёт латиницу в соответствии с Приказом МИД по транслитерации
# - Бот работает из-под docker контейнера

# Создаем объект бота
bot = Bot(token=TOKEN)

# Создаем объект диспетчера
# Все хэндлеры(обработчики) должны быть подключены к диспетчеру
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Hello, {user_name}!"
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply(text)

Обработчик будет пересылать полученное сообщение обратно отправителю

По умолчанию обработчик сообщений будет обрабатывать все типы сообщений (например, текст, фото, стикер и т.д.)

# Хэндлер на любые сообщения
@dp.message()
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f"{user_name=} {user_id=} sent message: {text}")
    await bot.send_message(user_id, text)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
