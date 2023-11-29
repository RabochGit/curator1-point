import telebot
bot = telebot.TeleBot('6700419125:AAHhol7uI5fzUCanKgl0tD27d4e873RtHzI')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет)', parse_mode='Markdown')

@bot.message_handler(commands=['red'])
def main(message):
    bot.send_message(message.chat.id, '*красный \nцвет*')

@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'Это [ССЫЛКА](http://viruzz.byethost12.com/LITERATURES/op&lit) на материал ', parse_mode='Markdown')

bot.infinity_polling()