import telebot
import time
bot = telebot.TeleBot
CHANNEL_NAME = ''
f = open('fun.txt','r',encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
for joke in jokes:
    bot.send_message(CHANNEL_NAME,joke)
    time.sleep(3600)
bot.send_message(CHANNEL_NAME,"anektodi nety")



