import telebot
from telebot import types
import random
bot=telebot.TeleBot('5671354753:AAHZoXr8NO3fxlHQKtRAfWVVDeCtxfqesqk')
numbers = [1,2,3]
rand = random.choice(numbers)
numbers2=range(1,5)
rand2=random.choice(numbers2)
numbers3=range(1,6)
rand3=random.choice(numbers3)
numbers4=range(1,7)
rand4=random.choice(numbers4)
numbers5=range(1,8)
rand5=random.choice(numbers5)
numbers6=range(1,9)
rand6=random.choice(numbers6)
@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, 'Hello stranger welcome to bagroulette\nThis is a telegram bot for fun ONLY\nChoose one button and then insert ur number by command /number')
@bot.message_handler(commands=["number"])
def get_debt(m):
    markup2 = types.InlineKeyboardMarkup(row_width=3)
    item_1 = types.InlineKeyboardButton('from 1 to 3', callback_data='1')
    item_2 = types.InlineKeyboardButton('from 1 to 4', callback_data='2')
    item_3 = types.InlineKeyboardButton('from 1 to 5', callback_data='3')
    item_4 = types.InlineKeyboardButton('from 1 to 6', callback_data='4')
    item_5 = types.InlineKeyboardButton('from 1 to 7', callback_data='5')
    item_6 = types.InlineKeyboardButton('from 1 to 8', callback_data='6')

    markup2.add(item_1,item_2,item_3,item_4,item_5,item_6)
    bot.send_message(m.chat.id,'choose your debt',reply_markup=markup2)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if call.message:
            if call.data=='1':
                bot.send_message(call.message.chat.id,'input your number from 1 to 3')
            @bot.message_handler(content_types=["text"])
            def times(message):
                if rand == int(message.text):
                    bot.send_message(message.chat.id, ''f' chosen number was {rand}')
                    bot.send_message(message.chat.id,'you won, congrats')

                else:
                    bot.send_message(message.chat.id, ''f' chosen number was {rand}')
                    bot.send_message(message.chat.id,'you lost better luck next time')
            if call.data=='2':
                bot.send_message(call.message.chat.id,'input your number from 1 to 4')
            @bot.message_handler(content_types=["text"])
            def times2(message):
                if rand2 == int(message.text):
                    bot.send_message(message.chat.id, ''f' chosen number was {rand2}')
                    bot.send_message(message.chat.id, "congrats you won")
                else:
                    bot.send_message(message.chat.id, ''f' chosen number was {rand2}')
                    bot.send_message(message.chat.id, 'you lost better luck next time')
            if call.data=='3':
                bot.send_message(call.message.chat.id,'input your number from 1 to 5')
            @bot.message_handler(content_types=["text"])
            def times2(message):
                if rand3 == int(message.text):
                    bot.send_message(message.chat.id, ''f' chosen number was {rand3}')
                    bot.send_message(message.chat.id, "congrats you won")
                else:
                    bot.send_message(message.chat.id, ''f' chosen number was {rand3}')
                    bot.send_message(message.chat.id, 'you lost better luck next time')
            if call.data=='4':
                bot.send_message(call.message.chat.id,'input your number from 1 to 6')
            @bot.message_handler(content_types=["text"])
            def times2(message):
                if rand4 == int(message.text):
                    bot.send_message(message.chat.id, ''f' chosen number was {rand4}')
                    bot.send_message(message.chat.id, "congrats you won")
                else:
                    bot.send_message(message.chat.id, ''f' chosen number was {rand4}')
                    bot.send_message(message.chat.id, 'you lost better luck next time')
            if call.data=='5':
                bot.send_message(call.message.chat.id,'input your number from 1 to 7')
            @bot.message_handler(content_types=["text"])
            def times2(message):
                if rand5 == int(message.text):
                    bot.send_message(message.chat.id, ''f' chosen number was {rand5}')
                    bot.send_message(message.chat.id, "congrats you won")
                else:
                    bot.send_message(message.chat.id, ''f' chosen number was {rand5}')
                    bot.send_message(message.chat.id, 'you lost better luck next time')
            if call.data=='6':
                bot.send_message(call.message.chat.id,'input your number from 1 to 8')
            @bot.message_handler(content_types=["text"])
            def times2(message):
                if rand6 == int(message.text):
                    bot.send_message(message.chat.id, ''f' chosen number was {rand6}')
                    bot.send_message(message.chat.id, "congrats you won")
                else:
                    bot.send_message(message.chat.id, ''f' chosen number was {rand6}')
                    bot.send_message(message.chat.id, 'you lost better luck next time')

bot.polling(none_stop=True,interval=0)