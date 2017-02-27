"""Prima prova per leggere database con indirizzi di foto."""
import random

batmanDB = open('batmanDB.txt', 'r')
# TODO: forse con file csv sarebbe leggermente più pulito
linee = 0
for line in batmanDB:
    linee = linee + 1
batmanDB.seek(0)    # Per tornare ad inizio file.
print('Numero di linee nel file: {}'.format(linee))

n_linea = random.randint(0, linee - 1)
print('Il numero estratto è: {}'.format(n_linea))
estratto = batmanDB.readlines()[n_linea].split(',')
print('Url: {}'.format(estratto[0]))
print('Caption: {}'.format(estratto[1].strip()))
batmanDB.close()
