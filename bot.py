import telebot
import requests

API_TOKEN = '7822913089:AAHC2dPksVN_I6keo-x7vbIDQim2DL0Ebbs'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])  
def start_message(message):
    bot.reply_to(message, "Привет, я бесплатный помошник по быстрому поиску музыки!")

@bot.message_handler(commands=['search'])
def send_music(message):
    search = message.text.replace("/search ", "")
    r = requests.get('https://mp3party.net/search?q={}'.format(search))
    
    



bot.infinity_polling()