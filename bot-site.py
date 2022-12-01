import telebot
from random import *
import json
import requests
import log
API_URL = 'https://7012.deeppavlov.ai/model'

API_TOKEN = '5952228267:AAE337fMtvBuxDvnXHnGLYRBpzWLwLjzdl8'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Готов к работе!")


@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    print(quest)
    qq = " ".join(quest)
    data = {'question_raw': [qq]}
    try:
        res = requests.post(API_URL, json=data, verify=False).json()
        result = bot.send_message(message.chat.id, res)
        log.result_log(message.text, result.text)
    except:
        bot.send_message(message.chat.id, 'Что-то я ничего не нашёл :-(')


bot.polling()
