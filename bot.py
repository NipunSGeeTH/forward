import telebot

# Replace with your bot token
BOT_TOKEN = '2118571380:AAGR-_rB53MsMon35q5i2B3Nw7RJqPXHy18'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.send_message(message.chat.id, 'Hi!')

bot.polling()
