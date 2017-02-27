"""" Prima prova del Bot in Telegram.

# seguita la guida in:
# https://github.com/python-telegram-bot/python-telegram-bot
# Nome del Bot: Sopresa
# Username: @KattyBot
# Token: 362591666:AAEwquW77vwbnwDhK2899SGUoW4emmKoLQk.
"""

# import logging
import random
import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import BaseFilter

flag_Chat = True
IDchat = 0
SpamID = {-2861403, 163078549}  # Netflix: -2861403  Marco: 163078549

updater = Updater(token='362591666:AAEwquW77vwbnwDhK2899SGUoW4emmKoLQk')

dispatcher = updater.dispatcher
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

"""Definizione di alcuni filtri base che bloccano le azioni del bot."""
class FilterSpam(BaseFilter):
    """Filtro da usare per limitare ad un gruppo l'uso del bot."""
    def filter(self, message):
        """Controlla che l'ID della chat sia uguale a quello dello Spam."""
        return message.chat_id in SpamID


class FilterOnOff(BaseFilter):
    """Filtro da usare per limitare ad un gruppo l'uso del bot."""
    def filter(self, message):
        """Controlla che l'ID della chat sia uguale a quello dello Spam."""
        return flag_Chat is True


filter_spam = FilterSpam()
filter_OnOff = FilterOnOff()

# TODO: creare un dizionario con coppia "chat ID" e "stato flag_Chat" e poi modificare il relativo filtro in modo che guardi lo stato della specifica chat.
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


""" ----------- COMANDO BATMAN --------------"""
def batman(bot, update):
    """La funzione callback che viene chiamata dalla parola chiave batman."""
    batmanDB = open('batmanDB.txt', 'r')
    linee = 0
    for line in batmanDB:
        linee = linee + 1
    batmanDB.seek(0)    # Per tornare ad inizio file.

    n_linea = random.randint(0, linee - 1)
    estratto = batmanDB.readlines()[n_linea].split(',')
    link = estratto[0]
    didascalia = estratto[1]
    batmanDB.close()

    bot.sendPhoto(chat_id=update.message.chat_id, photo=link, caption=didascalia)


class FilterBatman(BaseFilter):
    """Questa parte si occupa di verificare la presenza della parola chiave "batman" nel testo del messaggio. Se è presente, ritorna 1 e quindi viene chiamata la funzione di callback batman."""
    def filter(self, message):
        """Ritorna True se la parola batman è presente nel testo del messaggio."""
        return 'batman' in message.text.lower()


filter_batman = FilterBatman()

batman_handler = MessageHandler(filter_batman & filter_spam & filter_OnOff, batman)
dispatcher.add_handler(batman_handler, group=0)

""" ----------- COMANDO FILE LOCALE --------------"""
def foto(bot, update):
    """La funzione callback che viene chiamata dalla parola chiave batman."""
    lista_imm = os.listdir("immagini")
    n_imm = random.randint(0, len(lista_imm) - 1)
    bot.sendPhoto(update.message.chat_id, open("immagini/" + lista_imm[n_imm], 'rb'))

class FilterFoto(BaseFilter):
    """Questa parte si occupa di verificare la presenza della parola chiave "batman" nel testo del messaggio. Se è presente, ritorna 1 e quindi viene chiamata la funzione di callback batman."""
    def filter(self, message):
        """Ritorna True se la parola batman è presente nel testo del messaggio."""
        return 'foto locale' in message.text.lower()
        # TODO: cercare di rendere più di una le stringhe che attivato il callback


filter_foto = FilterFoto()

foto_handler = MessageHandler(filter_foto & filter_spam & filter_OnOff, foto)
dispatcher.add_handler(foto_handler, group=0)

""" ----------- COMANDO ECO --------------"""
def echo(bot, update):
    """Semplice comando: ogni volta che sniffa un messaggio, risponde con una frase."""
    bot.sendMessage(chat_id=update.message.chat_id, text='Ogni volta che scrivi qualcosa io rispondo così.')


echo_handler = MessageHandler(Filters.text & filter_spam & filter_OnOff, echo)
# dispatcher.add_handler(echo_handler, group=0)

# TODO: cercare come impostare un tempo limite oltre il quale non ripescare post
updater.start_polling(clean=True)

# Per terminare il bot: updater.stop()
# Per rimuovere handler: dispatcher.remove_handler(echo_handler)
