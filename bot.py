import telebot

API_TOKEN = '7822913089:AAHC2dPksVN_I6keo-x7vbIDQim2DL0Ebbs'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])  
def start_message(message):
    bot.reply_to(message, "Привет, я бесплатный помошник по быстрому поиску музыки!")

bot.infinity_polling()