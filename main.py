import time
import pathlib
import parser
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

           new_KWORKS = parser.KWORK(['11'])
           new_FL = parser.FL(["razrabotka-sajtov","programmirovanie"])
           new_cards = {**new_KWORKS,**new_FL}
           print(str(len(new_cards)) + " New at all")
           for option in new_cards:
                try:
                    head = option
                    address , describe , price , photo = new_cards[option][0],new_cards[option][1],new_cards[option][2],open(new_cards[option][3],"rb")
                    await bot.send_photo(920120916,photo,option)
                    photo.close()
                    await bot.send_message(920120916,describe + "\n" + price,reply_markup=button_url(address))
                    except_rem = ['Image/15s.png','Image/no.png', 'Image/16s.png' , 'Image/14s.png' , 'Image/17s.png' , 'Image/19s.png' , 'Image/18s.png' , 'Image/13s.png' , 'Image/12s.png']
                    if new_cards[option][3] not in except_rem:
                     try:
                        rem_file = pathlib.Path(new_KWORKS[option][3])
                        rem_file.unlink()
                     except:
                        pass
                except:
                    print("Error 403")
                    pass
                await asyncio.sleep(20)
           await asyncio.sleep(sleeping)
    print("Code error")
    return  m()



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(m(175))
    executor.start_polling(dp, skip_updates=True)
