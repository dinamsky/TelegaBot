import random

addioDB = open('addioDB.txt', 'r', encoding='utf-8')

linee = 0
for line in addioDB:
    linee = linee + 1
addioDB.seek(0)    # Per tornare ad inizio file.
print('Numero di linee nel file: {}'.format(linee))

n_linea = random.randint(0, linee - 1)
print('Il numero estratto è: {}'.format(n_linea))
estratto = addioDB.readlines()[n_linea]
print(estratto.format('CULO', u'\U0001F60D'))
addioDB.close()
