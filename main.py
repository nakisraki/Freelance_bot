import time
import pathlib
import asyncio
from aiogram import Bot, Dispatcher, types, executor

Token = "1855797574:AAGLUsUOi7QDoLcPmm3VEK7smPonDz8M7WU"
bot = Bot(token=Token)
dp = Dispatcher(bot=bot)

def button_url(link):
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.add(types.InlineKeyboardButton("Подробности", url=link))
    return keyboard_markup

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(message.chat.id)
    await message.reply("Мониторинг всех Freelance бирж")

async def m (sleeping):

    while True:

       print(a)
    print("Code error")
    return  m()



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(m(5))
    executor.start_polling(dp, skip_updates=True)
