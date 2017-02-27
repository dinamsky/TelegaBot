"""" Prima prova del Bot in Telegram.

# seguita la guida in:
# https://github.com/python-telegram-bot/python-telegram-bot
# Nome del Bot: Sopresa
# Username: @KattyBot
# Token: 362591666:AAEwquW77vwbnwDhK2899SGUoW4emmKoLQk.
"""

import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import BaseFilter

flag_Chat = True
IDchat = 0
SpamID = 163078549  # Marco: 163078549

updater = Updater(token='362591666:AAEwquW77vwbnwDhK2899SGUoW4emmKoLQk')

dispatcher = updater.dispatcher
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

"""Definizione di alcuni filtri base che bloccano le azioni del bot."""
class FilterSpam(BaseFilter):
    """Filtro da usare per limitare ad un gruppo l'uso del bot."""
    def filter(self, message):
        """Controlla che l'ID della chat sia uguale a quello dello Spam."""
        return SpamID == message.chat_id


class FilterOnOff(BaseFilter):
    """Filtro da usare per limitare ad un gruppo l'uso del bot."""
    def filter(self, message):
        """Controlla che l'ID della chat sia uguale a quello dello Spam."""
        return flag_Chat is True


filter_spam = FilterSpam()
filter_OnOff = FilterOnOff()


def start(bot, update):
    """Funzione chiamata da /start@KattyBot. Penso sia necessario chiamarla una volta. Oltre a scrivere un saluto, imposta anche il flag su True e questo viene usato per abilitare il resto delle conversazioni."""
    global flag_Chat
    bot.sendMessage(chat_id=update.message.chat_id, text="Ciao a tutti! KAFFFEEH?")
    flag_Chat = True


def stop(bot, update):
    """"Funzione chiamata da /stop@KattyBot. Oltre a scrivere un addio, imposta anche il flag su False."""
    global flag_Chat
    bot.sendMessage(chat_id=update.message.chat_id, text="Me ne vado. Ma prima voglio dire una cosa: A Beppe piace la Kattyyyy")
    flag_Chat = False


start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)


""" ----------- COMANDO BATMAN --------------"""
def batman(bot, update):
    """La funzione callback che viene chiamata dalla parola chiave batman."""
    bot.sendPhoto(chat_id=update.message.chat_id, photo='https://selfie.legobatman.com/assets/img/BatmanLegalScreen.png', caption='NANANANA')


class FilterBatman(BaseFilter):
    """Questa parte si occupa di verificare la presenza della parola chiave "batman" nel testo del messaggio. Se è presente, ritorna 1 e quindi viene chiamata la funzione di callback batman."""
    def filter(self, message):
        """Ritorna True se la parola batman è presente nel testo del messaggio."""
        return 'batman' in message.text


filter_batman = FilterBatman()

batman_handler = MessageHandler(filter_batman & filter_spam & filter_OnOff, batman)
dispatcher.add_handler(batman_handler, group=0)


""" ----------- COMANDO ECO --------------"""
def echo(bot, update):
    """Semplice comando: ogni volta che sniffa un messaggio, risponde con una frase."""
    bot.sendMessage(chat_id=update.message.chat_id, text='Ogni volta che scrivi qualcosa io rispondo così.')


echo_handler = MessageHandler(Filters.text & filter_spam & filter_OnOff, echo)
dispatcher.add_handler(echo_handler, group=0)


""" ----------- COMANDO CHAT ID --------------"""
def chatID(bot, update):
    """Questo è handler vuoto che uso solo per capire l'ID della chat,
    quando qualcuno scrive il comando /chat_id."""
    global IDchat
    user = update.message.from_user
    IDchat = update.message.chat.id
    print('Stai parlando con {} {}, il suo nickname è {} e il suo ID è {}.'.format(user['first_name'], user['last_name'], user['username'], user['id']))
    bot.sendMessage(chat_id=update.message.chat_id, text='Il chat ID è: ' + str(update.message.chat_id))


chatID_handler = CommandHandler('chatID', chatID)
dispatcher.add_handler(chatID_handler)


updater.start_polling(clean=True)

# Per terminare il bot: updater.stop()
# Per rimuovere handler: dispatcher.remove_handler(echo_handler)
