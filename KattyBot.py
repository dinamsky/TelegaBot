"""" Prima prova del Bot in Telegram.

# seguita la guida in:
# https://github.com/python-telegram-bot/python-telegram-bot
# Nome del Bot: Sopresa
# Username: @KattyBot
# Token: 362591666:AAEwquW77vwbnwDhK2899SGUoW4emmKoLQk.
"""

# import logging
import random
from datetime import datetime as dt
import time
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import BaseFilter

flag_Chat = True
IDchat = 0
AuthID = {-2861403, 163078549}  # Netflix: -2861403  Marco: 163078549
SpamID = 163078549  # Andrà cambiato con il vero SpamID
ChatID = {-2861403: True, 163078549: True}

listaKatty = ['katty', 'ketty', 'gnocca', 'figa',
              'cagna', 'tette', 'mozzarellona', 'culo', 'porca']
listaAddio = ['lascio', 'addio', 'vomito', 'schifo', 'oddio']

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class FilterSpam(BaseFilter):
    """Filtro da usare per limitare ad un gruppo l'uso del bot."""

    def filter(self, message):
        """Controlla che l'ID della chat sia uguale a quello dello Spam."""
        return message.chat_id in AuthID


class FilterOnOff(BaseFilter):
    """Filtro da usare per non abilitare la conversazione del bot."""

    def filter(self, message):
        """Controlla che l'ID della chat sia uguale a quello dello Spam."""
        return ChatID[message.chat_id]


def start(bot, update):
    """Funzione chiamata da /start@KattyBot. Penso sia necessario chiamarla una volta. Oltre a scrivere un saluto, imposta anche il flag su True e questo viene usato per abilitare il resto delle conversazioni."""
    global ChatID
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Ciao a tutti! KAFFFEEH?")
    # if not(update.message.chat_id in ChatID.keys()):
    ChatID[update.message.chat_id] = True


def stop(bot, update):
    """"Funzione chiamata da /stop@KattyBot. Oltre a scrivere un addio, imposta anche il flag su False."""
    global ChatID
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Me ne vado. Ma prima voglio dire una cosa: A Beppe piace la Kattyyyy")
    ChatID[update.message.chat_id] = False


def chatID(bot, update):
    """Questo è handler vuoto che uso solo per capire l'ID della chat, quando qualcuno scrive il comando /chatID."""
    global IDchat
    user = update.message.from_user
    IDchat = update.message.chat.id
    print('Stai parlando con {} {}, il suo nickname è {} e il suo ID è {}.'.format(
        user['first_name'], user['last_name'], user['username'], user['id']))
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Il chat ID è: ' + str(update.message.chat_id))


def katty(bot, update):
    """La funzione callback che viene chiamata dalla parola chiave katty."""
    kattyDB = open('kattyDB.txt', 'r')
    linee = 0
    for line in kattyDB:
        linee = linee + 1
    kattyDB.seek(0)    # Per tornare ad inizio file.
    n_linea = random.randint(0, linee - 1)
    estratto = kattyDB.readlines()[n_linea]
    kattyDB.close()
    bot.sendPhoto(chat_id=update.message.chat_id, photo=estratto)
    global timeKatty
    timeKatty = dt.now()
    # bot.sendPhoto(chat_id=update.message.chat_id, photo=estratto)


class FilterKatty(BaseFilter):
    """Questa parte si occupa di verificare la presenza della parola chiave "katty" nel testo del messaggio. Se è presente, ritorna 1 e quindi viene chiamata la funzione di callback katty."""

    def filter(self, message):
        """Ritorna True se la parola katty è presente nel testo del messaggio."""
        return any(parola in message.text.lower() for parola in listaKatty)


def addio(bot, update):
    """La funzione callback che viene chiamata dalla parola chiave addio e simili."""
    addioDB = open('addioDB.txt', 'r', encoding='utf-8')

    linee = 0
    for line in addioDB:
        linee = linee + 1
    addioDB.seek(0)    # Per tornare ad inizio file.

    n_linea = random.randint(0, linee - 1)
    estratto = addioDB.readlines()[n_linea]
    addioDB.close()

    user = update.message.from_user
    frase = estratto.format(user['first_name'], u'\U0001F60D')
    bot.sendMessage(chat_id=update.message.chat_id, text=frase)
    # 'Non dire così. Io ti AMO, {}!! {}'.format(user['first_name'], u'\U0001F60D'


class FilterAddio(BaseFilter):
    """Questa parte si occupa di verificare la presenza della parola chiave "addio" nel testo del messaggio. Se è presente, ritorna 1 e quindi viene chiamata la funzione di callback addio."""

    def filter(self, message):
        """Ritorna True se la parola addio è presente nel testo del messaggio."""
        controllo = (dt.now() - timeKatty).total_seconds() <= 5 * 60
        return any(parola in message.text.lower() for parola in listaAddio) and controllo

def main():
    """Impostazione di tutto."""
    # TODO: cercare come impostare un tempo limite oltre il quale non
    # ripescare post
    updater = Updater(token='362591666:AAEwquW77vwbnwDhK2899SGUoW4emmKoLQk')

    dispatcher = updater.dispatcher

    filter_spam = FilterSpam()
    filter_OnOff = FilterOnOff()
    filter_katty = FilterKatty()
    filter_addio = FilterAddio()

    start_handler = CommandHandler('start', start)
    stop_handler = CommandHandler('stop', stop)
    chatID_handler = CommandHandler('chatID', chatID)
    katty_handler = MessageHandler(
        filter_katty & filter_spam & filter_OnOff, katty)
    addio_handler = MessageHandler(
        filter_addio & filter_spam & filter_OnOff, addio)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(stop_handler)
    dispatcher.add_handler(chatID_handler)
    dispatcher.add_handler(katty_handler, group=0)
    dispatcher.add_handler(addio_handler, group=0)

    updater.start_polling(clean=True)
    # Per terminare il bot: updater.stop()
    # Per rimuovere handler: dispatcher.remove_handler(echo_handler)

    Notte = '00:30:00'
    Giorno = 7  # Domenica
    oraNotte = dt.strptime(Notte, '%H:%M:%S').time()
    while True:
        if dt.now().isoweekday() == Giorno and dt.now().time().replace(microsecond=0) == oraNotte:
            telegram.Bot(token='362591666:AAEwquW77vwbnwDhK2899SGUoW4emmKoLQk').sendPhoto(
                chat_id=SpamID, photo="https://scontent-mxp1-1.xx.fbcdn.net/v/t1.0-0/p206x206/1934853_1153771018060_4396368_n.jpg?oh=2bab7bd98f157337abbc4274bb639891&oe=593CF274", caption="Sogni d'oro, Beppe! {}".format(u'\U0001F618'))
            time.sleep(1)

    updater.idle()


if __name__ == '__main__':
    main()
