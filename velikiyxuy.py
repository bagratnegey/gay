import random
import telebot
from telebot import types
bot=telebot.TeleBot('5671354753:AAHZoXr8NO3fxlHQKtRAfWVVDeCtxfqesqk')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'hello and welcome to telegram channel bagroulette\nRules are simple as bycicle, you debt money on a number, if you guess it you are getting 2x and money back of debt cash back, if not we will take 2x of your cash debt\nenjoy!  )')
curency = 1000
debt = 0
debt2 = debt*2+curency
debt3= curency-debt*2
numbers = range(1,2)
rand = random.choice(numbers)
@bot.message_handler(commands=["debt"])
def get_debt(m, res=False):
    markup2 = types.InlineKeyboardMarkup(row_width=3)
    item_1 = types.InlineKeyboardButton('10', callback_data='10')
    item_2 = types.InlineKeyboardButton('30', callback_data='30')
    item_3 = types.InlineKeyboardButton('50', callback_data='50')
    item_4 = types.InlineKeyboardButton('80', callback_data='80')
    item_5 = types.InlineKeyboardButton('100', callback_data='100')
    item_6 = types.InlineKeyboardButton('250', callback_data=250)
    item_7 = types.InlineKeyboardButton('500(high amount of risk!)', callback_data='500')
    item_8 = types.InlineKeyboardButton('1000(we dont recomend betting this amount of money)', callback_data='1000')
    item_9 = types.InlineKeyboardButton('400', callback_data='400')
    markup2.add(item_1,item_2,item_3,item_4,item_5,item_6,item_7,item_8,item_9)
    bot.send_message(m.chat.id,'choose your debt',reply_markup=markup2)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data=='10':
            bot.send_message(call.message.chat.id,''f' your chosen number is {10}')
        elif call.data=='30':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {30}')
        elif call.data == '50':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {50}')
        elif call.data=='80':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {80}')
        elif call.data=='100':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {100}')
        elif call.data=='250':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {250}')
        elif call.data == '400':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {400}')
        elif call.data=='500':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {500}')
        elif call.data=='1000':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {1000}')
@bot.message_handler(commands=['button'])
def button(message):
    bot.send_message(message.chat.id,'input your number in from 1 to 6')
@bot.message_handler(content_types=["text"])
def times(message):
    if rand == int(message.text):
        bot.send_message(message.chat.id, "congrats you won")
        bot.send_message(message.chat.id,debt2)
    else:
        bot.send_message(message.chat.id,'you lost')
        bot.send_message(message.chat.id,debt3)


bot.polling(none_stop=True,interval=0)


