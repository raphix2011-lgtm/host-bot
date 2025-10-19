import telebot
from telebot import types
import threading
from flask import Flask
import requests
import os
import time

# 🔹 Твой токен бота
BOT_TOKEN = "8369428916:AAEhjphFbIoazRN1j6H046lUHtKZi7cfpqI"
bot = telebot.TeleBot(BOT_TOKEN)

# =======================
# Flask сервер для keep_alive
# =======================
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive!"

def keep_alive():
    url = os.environ.get("SELF_URL")  # URL Render, например: https://your-bot.onrender.com
    while True:
        try:
            if url:
                requests.get(url)
        except:
            pass
        time.sleep(600)  # каждые 10 минут

# =======================
# Команда /start
# =======================
@bot.message_handler(commands=['start'])
def start(message):
    # 🔹 Кнопка WebApp
    webapp_btn = types.WebAppInfo("https://raphix2011-lgtm.github.io/tooclickerbot/")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🚀 Открыть игру", web_app=webapp_btn))

    # 🔹 Приветствие
    bot.send_message(
        message.chat.id,
        "👋 Привет! Это *Not Stars Bot* — твой помощник и кликер.\n\n"
        "🔗 Нажми кнопку ниже, чтобы открыть WebApp:",
        parse_mode="Markdown",
        reply_markup=markup
    )

# =======================
# Запуск keep_alive и polling
# =======================
if __name__ == "__main__":
    # Запуск сервера Flask в отдельном потоке
    threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": int(os.environ.get("PORT", 5000))}).start()
    # Запуск пинга самого себя
    threading.Thread(target=keep_alive, daemon=True).start()
    # Запуск бота
    bot.infinity_polling()
    
