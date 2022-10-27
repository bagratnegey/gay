import random
import telebot
bot=telebot.TeleBot('')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'hello and welcome to telegram channel bagroulette\nRules are simple as bycicle, you debt money on a number, if you guess it you are getting 2x and money back of debt cash back, if not we will take 2x of your cash debt\nenjoy!\nUse command /button to proceed  )')
numbers = [1,2,3,4,5,6]
rand = random.choice(numbers)
@bot.message_handler(commands=['button'])
def button(message):
    bot.send_message(message.chat.id,'input your number in from 1 to 6')
@bot.message_handler(content_types=["text"])
def times(message):
    if rand == int(message.text):
        bot.send_message(message.chat.id, "congrats you won")
    else:
        bot.send_message(message.chat.id,'you lost')
@bot.message_handler(context_types=['text'])
def num(m):
    bot.send_message(m.chat.id,f'rand')
bot.polling(none_stop=True,interval=0)