""" ----------- COMANDO BATMAN --------------"""
listaBatman = ['batman', 'robin', 'dc', 'nananana']

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
        return any(parola in message.text.lower() for parola in listaBatman)


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


filter_foto = FilterFoto()

foto_handler = MessageHandler(filter_foto & filter_spam & filter_OnOff, foto)
dispatcher.add_handler(foto_handler, group=0)

""" ----------- COMANDO ECO --------------"""
def echo(bot, update):
    """Semplice comando: ogni volta che sniffa un messaggio, risponde con una frase."""
    bot.sendMessage(chat_id=update.message.chat_id, text='Ogni volta che scrivi qualcosa io rispondo così.')


echo_handler = MessageHandler(Filters.text & filter_spam & filter_OnOff, echo)
# dispatcher.add_handler(echo_handler, group=0)
