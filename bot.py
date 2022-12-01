import telebot
from random import *
import json
import log
import rational

calc = False

API_TOKEN = '5952228267:AAE337fMtvBuxDvnXHnGLYRBpzWLwLjzdl8'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Готов к работе!")


@bot.message_handler(commands=['calc'])
def calc_message(message):
    global calc
    calc = True
    bot.send_message(message.chat.id, "Введите выражение для вычисления")


@bot.message_handler(content_types='text')
def message_reply(message):
    global calc
    if 'привет' in message.text:
        bot.send_message(message.chat.id, 'И тебе привет')
    if calc:
        result = bot.send_message(message.chat.id, rational.rational(message.text))
        log.result_log(message.text, result.text)
    else:
        result = bot.send_message(message.chat.id, eval(message.text))
        log.result_log(message.text, result.text)

bot.polling()
