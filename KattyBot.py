# Prima prova del Bot in Telegram.
# seguita la guida in:
# https://github.com/python-telegram-bot/python-telegram-bot
# Nome del Bot: Sopresa
# Username: @KattyBot
# Token: 362591666:AAEwquW77vwbnwDhK2899SGUoW4emmKoLQk

import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import BaseFilter

updater = Updater(token='362591666:AAEwquW77vwbnwDhK2899SGUoW4emmKoLQk')

dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Teo SUKA!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
# Per chiamare questo comando è sufficiente nella chat di
# Telegram scrivere /start@KattyBot


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Ogni volta che scrivi qualcosa io rispondo così.')


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
# dispatcher.remove_handler(echo_handler)

def batman(bot, update):
    bot.sendPhoto(chat_id=update.message.chat_id, photo='https://selfie.legobatman.com/assets/img/BatmanLegalScreen.png')


class FilterBatman(BaseFilter):
    def filter(self, message):
        return 'batman' in message.text


filter_batman = FilterBatman()

batman_handler = MessageHandler(filter_batman, batman)
dispatcher.add_handler(batman_handler)

# Questo è handler vuoto che uso solo per capire l'ID della chat,
# quando qualcuno scrive il comando /chat_id
def chat_id(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.chat_id)

class FilterChatID(BaseFilter):
    def filter(self, message):
        return 'chat_id' in message.text


filter_chat = FilterChatID()

chatID_handler = CommandHandler(filter_chat, chat_id)
dispatcher.add_handler(chatID_handler)

updater.start_polling()

# Per terminare il bot: updater.stop()
