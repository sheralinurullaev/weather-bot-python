import telebot
import requests
import json
from telebot import types

bot = telebot.TeleBot('ваш токен')
API = 'ваш токен'

@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(message.chat.id, f"Здравствуйте {message.from_user.first_name}, я бот для получения погоды. Чтобы получить погоду в нужном для вас местоположении просто введите название города!")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f'Сейчас погода {data["main"]["temp"]} ')
    else:
        bot.reply_to(message, "Город указан не верно!")

bot.infinity_polling()
