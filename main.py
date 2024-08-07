import telebot

bot = telebot.TeleBot("7297532473:AAGw4CG7M8mSVmSyC_LAT2qd2MyExsKv0lQ")


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет, для начала изучения или повторения выбери /period")


@bot.message_handler(commands=["period"])
def start_handler(message):
    bot.send_message(message.chat.id,
                     "Выберите исторический период, который хотите изучить или повторить: Древняя Русь — команда /DrevnyaRus")


@bot.message_handler(commands=["DrevnyaRus"])
def start_handler(message):
    bot.send_message(message.chat.id, "Добро пожаловать в блок Древняя Русь. Первая дата 1097 — Любечский съезд")


@bot.message_handler(commands=["meow"])
def start_handler(message):
    bot.send_message(message.chat.id, "зачем тебе мяу")


bot.infinity_polling()
