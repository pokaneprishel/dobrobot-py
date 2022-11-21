import telebot
from telebot import types
import random


bot = telebot.TeleBot('5714234655:AAHKmnjG-FUORLvicJM6hnqqHW1oly4BPNQ')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Welcome, <b>{message.from_user.first_name}!</b>'
    bot.send_message(
        message.chat.id, f'Приветствую, <b>{message.from_user.first_name}:) </b> Судя по вашим логам - вы прекрасны!', parse_mode='html')
    sticker = open('stic/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, f'Hi!', parse_mode='html')
    elif message.text == 'Привет':
        bot.send_message(message.chat.id, f'Привет!', parse_mode='html')
    elif message.text == 'Hi':
        bot.send_message(message.chat.id, f'Hi!', parse_mode='html')
    elif message.text == 'Спасибо':
        bot.send_message(
            message.chat.id, f'Рад стараться для вас :)', parse_mode='html')
    elif message.text == 'Thanks':
        bot.send_message(message.chat.id, f'Glad to try fo you :)',
                        parse_mode='html')
    elif message.text == 'Как настроение?':
        bot.send_message(message.chat.id, f'Мое настроение всегда рабочее!',
                        parse_mode='html')
    elif message.text == 'Ты не устал?':
        bot.send_message(message.chat.id, f'Машины не знают усталости, увы',
                        parse_mode='html')
    elif message.text == 'Кто твой создатель?':
        bot.send_message(message.chat.id, f'Вы имеете ввиду Основатель? ;)',
                        parse_mode='html')
    elif message.text == 'Зачем тебя создали?':
        bot.send_message(message.chat.id, f'Я тоже задаюсь эти вопросом...',
                        parse_mode='html')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, f'Приятно было провести с вами время :)',
                        parse_mode='html')
    else:
        bot.send_message(
            message.chat.id, f"Извини, с этим лучше к человекам", parse_mode='html')


bot.polling(non_stop=True)
