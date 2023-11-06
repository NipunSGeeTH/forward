import telegram
from telegram.ext import Updater, CommandHandler, Filters

updater = Updater('2118571380:AAGR-_rB53MsMon35q5i2B3Nw7RJqPXHy18')
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text('Hi!')

dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
