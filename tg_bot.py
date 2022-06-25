import telebot
from main.models import *


bot = telebot.TeleBot("5411411957:AAHytHjnViT_oOvirMHa1H_1P_RSBCctH5U", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not TelegramUser.objects.filter(tg_id=message.chat.id):
        TelegramUser.objects.create(tg_id=message.chat.id)
        bot.send_message(message.chat.id, "Привет, человек! Теперь я буду писать тебе всё, чего я только пожелаю :)")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Тебе никто не поможет :D")


def start():
    bot.infinity_polling()