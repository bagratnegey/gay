import random
import telebot
from telebot import types
bot=telebot.TeleBot('5671354753:AAHZoXr8NO3fxlHQKtRAfWVVDeCtxfqesqk')

@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, 'hello and welcome to telegram channel bagroulette\nRules are simple as bycicle, you debt money on a number, if you guess it you are getting 2x and money back of debt cash back, if not we will take 2x of your cash debt\nenjoy!\nUse command /debt to proceed  )')
curency = 1000
debt = 0
debt2 = debt*2+curency
debt3= curency-debt*2
numbers = range(1,2)
rand = random.choice(numbers)
@bot.message_handler(commands=['debt'])
def debt(message):
    bot.send_message(message.chat.id,'input your debt from 1 to 1000')
@bot.message_handler(content_types=["text"])
def debt2(message):
    if debt < int(message.text):
        bot.send_message(message.chat.id, "your chosen number is")
        bot.send_message(message.chat.id,message)
@bot.message_handler(commands=['button'])
def button(message):
    bot.send_message(message.chat.id,'input your number in from 1 to 6')
@bot.message_handler(content_types=["text"])
def times(message):
    if rand == int(message.text):
        bot.send_message(message.chat.id, "congrats you won, your curency will show up after this message ")
        bot.send_message(message.chat.id,debt2)
    else:
        bot.send_message(message.chat.id,'you lost,your curency will show up after this message')
        bot.send_message(message.chat.id,debt3)


bot.polling(none_stop=True,interval=0)


