# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor


# bot = Bot(token= "5344213987:AAFfJCqwq8fR-4oZpzi54bu3XGqnCywg0oM")
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Добро пожаловать. Мы школа IT, у нас есть такие команды как /help, /info")

# @dp.message_handler(commands=['info'])
# async def process_help_command(message: types.Message):
#     await message.reply("Моско́вский госуда́рственный университе́т и́мени М. В. Ломоно́сова — один из старейших и крупнейших классических университетов России, один из центров российской науки и культуры, расположенный в Москве. C 1940 года носит имя Михаила Васильевича Ломоносова.")


# @dp.message_handler(commands = ['help'])
# async def help_command(message: types.Message):
#     await message.reply("У нас есть такие комманды как /help, /info")

# @dp.message_handler()
# async def echo(message: types.Message):
#     await bot.send_message(message.from_user.id, "Я не понимаю вас, введиет /start для полной информации")  


# if __name__ == '__main__':
#     executor.start_polling(dp)



from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token= "5344213987:AAFfJCqwq8fR-4oZpzi54bu3XGqnCywg0oM")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Добро пожаловать! Я содержу полную информацию о композиторе Фредерик Шопен!  А так же уменя есть такие функции:/help, /info")

@dp.message_handler(commands=['info'])
async def process_help_command(message: types.Message):
    await message.reply("Фридери́к Шопе́н дата рождения: 1 марта 1810, деревня Желязова-Воля, близ Варшавы, Варшавское герцогство. Дата смерти — 17 октября 1849, Париж, Франция) — польский композитор и пианист французско-польского происхождения. В зрелые годы (с 1831 года) жил и работал во Франции. Один из ведущих представителей западноевропейского музыкального романтизма, основоположник польской национальной композиторской школы. Оказал значительное влияние на мировую музыку.  /help /")


@dp.message_handler(commands = ['help'])
async def help_command(message: types.Message):
    await message.reply("У нас есть такие комманды как /help, /info")

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, "Я не понимаю вас, введиет /start для полной информации")  


if __name__ == '__main__':
    executor.start_polling(dp)


