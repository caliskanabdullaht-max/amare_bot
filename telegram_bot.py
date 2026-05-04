import telebot
from message_flow import get_intro_message, get_followup_message
from config import TELEGRAM_TOKEN


bot = telebot.TeleBot(TELEGRAM_TOKEN
)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    if text in ["merhaba", "selam"]:
        bot.reply_to(message, get_intro_message())
    else:
        bot.reply_to(message, get_followup_message(text))

bot.polling()
