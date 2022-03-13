import telebot
from telebot import types
import datetime
import wikipedia, re
token = "5175610928:AAFRiVFrQMciTMV5-lCDfIihDaVOA6k0uB4"
bot = telebot.TeleBot(token)
wikipedia.set_lang("ru")


def wik(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
            return 'В энциклопедии нет информации об этом'


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Date", "/Time", "/News", "/help",)
    bot.send_message(message.chat.id, "Отправьте мне любое слово, и я найду его значение на Wikipedia", reply_markup=keyboard)


@bot.message_handler(commands=["help"])
def start_message(message):
    bot.send_message(message.chat.id, "Я могу найти любую информацию в Wikipedia которая вас может заинтересовать. \n\nВозможные команды:\n/Time - Для вывода точного времени \n/Date - для вывода точной даты \n/News - для вывода новостей " )


@bot.message_handler(commands=["Date"])
def date_message(message):
    Date = datetime.datetime.now()
    dt = Date.strftime("Дата: %d/%m/%Y")
    bot.send_message(message.chat.id, dt)


@bot.message_handler(commands=["Time"])
def time_message(message):
    Date = datetime.datetime.now()
    vr = Date.strftime("Время: %H:%M:%S")
    bot.send_message(message.chat.id, vr)


@bot.message_handler(commands=["News"])
def news_message(message):
    bot.send_message(message.chat.id, 'https://tass.ru')


@bot.message_handler(content_types=["text"])
def wik2(message):
    bot.send_message(message.chat.id, wik(message.text))


bot.polling(none_stop=True, interval=0)
