import random
import telebot
from telebot import types
bot=telebot.TeleBot('5671354753:AAHZoXr8NO3fxlHQKtRAfWVVDeCtxfqesqk')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'hello and welcome to telegram channel bagroulette\nRules are simple as bycicle, you debt money on a number, if you guess it you are getting 2x and money back of debt cash back, if not we will take 2x of your cash debt\nenjoy!  )')
curency = 1000

debt_1= 10
debt_2= 30
debt_3=50
debt_4=100
debt_5=250
debt_6=400
debt_7=500
debt_8=1000
debt_9=80
debt = [debt_1,debt_2,debt_3,debt_4,debt_5,debt_6,debt_7,debt_8,debt_9]
numbers = range(1,7)
rand = random.choice(numbers)
@bot.message_handler(context_types=['text'])
def proceed(message):
    bot.send_message(message.chat.id,'input your number')
@bot.message_handler(commands=["debt"])
def get_debt(m, res=False):
    markup2 = types.InlineKeyboardMarkup(row_width=3)
    item_1 = types.InlineKeyboardButton('10', callback_data='10')
    item_2 = types.InlineKeyboardButton('30', callback_data='30')
    item_3 = types.InlineKeyboardButton('50', callback_data='50')
    item_4 = types.InlineKeyboardButton('80', callback_data='80')
    item_5 = types.InlineKeyboardButton('100', callback_data='100')
    item_6 = types.InlineKeyboardButton('250', callback_data='250')
    item_7 = types.InlineKeyboardButton('500(high amount of risk!)', callback_data='500')
    item_8 = types.InlineKeyboardButton('1000(we dont recomend betting this amount of money)', callback_data='1000')
    item_9 = types.InlineKeyboardButton('400', callback_data='400')
    markup2.add(item_1,item_2,item_3,item_4,item_5,item_6,item_7,item_8,item_9)
    bot.send_message(m.chat.id,'choose your debt',reply_markup=markup2)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data=='10':
            bot.send_message(call.message.chat.id,'10')
        elif call.data=='30':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {30}')
            debt=30
        elif call.data == '50':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {50}')
            debt=50
        elif call.data=='80':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {80}')
            debt=50
        elif call.data=='100':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {100}')
            debt=100
        elif call.data=='250':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {250}')
            debt=250
        elif call.data == '400':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {400}')
            debt=400
        elif call.data=='500':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {500}')
            debt=500
        elif call.data=='1000':
            bot.send_message(call.message.chat.id, ''f' your chosen number is {1000}')
            debt=1000




debt2 = debt*2+curency
debt3= debt/2+curency
@bot.message_handler(commands=['button'])
def button(message):
    bot.send_message(message.chat.id,'input your number in from 1 to 6')
@bot.message_handler(content_types=["text"])
def times(message):
    if rand == int(message.text):
        bot.send_message(message.chat.id, "congrats you won")
        bot.send_message(message.chat.id,f'you balance is{debt2}')
    else:
        bot.send_message(message.chat.id,'you lost')
        bot.send_message(message.chat.id, f'you balance is{debt3}')
bot.polling(none_stop=True,interval=0)

