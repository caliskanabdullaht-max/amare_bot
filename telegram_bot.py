import telebot
from message_flow import get_intro_message, get_followup_message
from config import 8747215307:AAHe7dRa_pNLU_BO6pRjnMP7NpiSsRy8VzQ

bot = telebot.TeleBot(8747215307:AAHe7dRa_pNLU_BO6pRjnMP7NpiSsRy8VzQ)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    if text in ["merhaba", "selam"]:
        bot.reply_to(message, get_intro_message())
    else:
        bot.reply_to(message, get_followup_message(text))

bot.polling()
