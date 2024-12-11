from bs4 import BeautifulSoup
import telebot
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

API_TOKEN = '7822913089:AAHC2dPksVN_I6keo-x7vbIDQim2DL0Ebbs'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])  
def start_message(message):
    bot.reply_to(message, "Привет, я бесплатный помошник по быстрому поиску музыки!")

@bot.message_handler(commands=['search'])
def send_music(message):
    search = message.text.replace("/search ", "")
    bot.reply_to(message, "Результаты поиска по запросу {}".format(search))
    r = requests.get('https://mp3party.net/search?q={}'.format(search))

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        elements = soup.find_all(class_='track__title js-track-title')

        if elements == []:
            bot.reply_to(message, "По вашему запросу ничего не найдено...")
        else:
            for element in elements:
                song_href = element.get('href')
                if not song_href:
                    continue

                song_id = element.get('href').replace("/music/", "")
                r = requests.get('https://dl2.mp3party.net/download/{}'.format(song_id), stream=True, headers=headers)
                if r.status_code == 200:
                    with open('file.mp3', 'wb') as file:
                        for chunk in r.iter_content(chunk_size=32768):
                            file.write(chunk)
                    with open('file.mp3', 'rb') as file:
                        bot.send_audio(message.chat.id, file)

                    del file
                    

    
    



bot.infinity_polling()