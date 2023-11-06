import telebot

# Replace with your bot token
BOT_TOKEN = '2118571380:AAGR-_rB53MsMon35q5i2B3Nw7RJqPXHy18'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['text', 'sticker', 'photo', 'audio', 'document', 'video', 'animation'])
def forward_message(message):
    if message.content_type == 'text':
        bot.send_message(message.chat.id, message.text)
    elif message.content_type == 'sticker':
        bot.send_sticker(message.chat.id, message.sticker.file_id)
    elif message.content_type == 'photo':
        bot.send_photo(message.chat.id, message.photo[-1].file_id)
    elif message.content_type == 'audio':
        bot.send_audio(message.chat.id, message.audio.file_id)
    elif message.content_type == 'document':
        bot.send_document(message.chat.id, message.document.file_id)
    elif message.content_type == 'video':
        bot.send_video(message.chat.id, message.video.file_id)
    elif message.content_type == 'animation':
        bot.send_animation(message.chat.id, message.animation.file_id)

bot.polling()
