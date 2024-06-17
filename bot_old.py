# Статус:
# 1. транслит не работает. Без докера. Проверить тут https://t.me/latin2cyr06_bot плюс, Эта функция требует базового языка - можно без этого? # type: ignore
# 2. про докер - создала много штук, при попытке выполнения они тут же exit через полсекунды. Токен не нравится.
# 3. вопрос: когда поллинг запущен, то терминал не работает как обычно. Как пользоваться термииналом?
# 4. инструкция по запуску в readme - на основе чего мне понять, как ее записать? ну и как ее записать.


# 1.Импорт библиотек
import logging
import transliterate
import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message             
from aiogram.filters.command import Command   # обрабатываем команды /start, /help и другие

# # # 2. Инициализация объектов
bot = Bot(token='7412105233:AAEpjHUyIGMN7c6Tw5Zj8ejEcpuYsx7YSQo')
# TOKEN = os.getenv('TOKEN')
# bot = Bot(token=TOKEN)                        
dp = Dispatcher()                             
logging.basicConfig(level=logging.INFO)        # аргумент - второй уровень 
logging.basicConfig(filename = "log.txt")


# # # 3. Обработка/Хэндлер на команду /start
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Hi there, {user_name}!'
    logging.info(f'{user_name} {user_id} started the bot')
    await bot.send_message(chat_id=user_id, text=text)
    
# # 4. Обработка/Хэндлер на любые сообщения
@dp.message()
async def transliterate_message(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    # text = message.text 
    transliterated_text = translit(message.text, 'ru', reversed=True)
    # вопрос - он требует язык, а это ж непраивльно? можно без этого?
    logging.info(f'{user_name} {user_id}: {transliterated_text}')
    await message.answer(text=transliterated_text)
    with open('log.txt', 'a') as log_file:
        log_file.write(f'{message.from_user.id}: {message.text} -> {transliterated_text}\n')

# # 5. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)

