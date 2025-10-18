import telebot
from telebot import types

# 🔹 Твой токен бота
BOT_TOKEN = "8369428916:AAEhjphFbIoazRN1j6H046lUHtKZi7cfpqI"
bot = telebot.TeleBot(BOT_TOKEN)

# 🔹 Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    # Кнопка WebApp
    webapp_btn = types.WebAppInfo("https://raphix2011-lgtm.github.io/tooclickerbot/")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🚀 Открыть игру", web_app=webapp_btn))

    # Приветствие
    bot.send_message(
        message.chat.id,
        "👋 Привет! Это *Not Stars Bot* — твой помощник и кликер.\n\n"
        "🔗 Нажми кнопку ниже, чтобы открыть WebApp:",
        parse_mode="Markdown",
        reply_markup=markup
    )

# 🔹 Запуск
bot.infinity_polling()