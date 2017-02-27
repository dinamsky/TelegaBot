""" Prova file locali.
Con questo si prova il sistema di generazione di una lista di nomi di files nella cartella e una estrazione automatica di uno di questi a caso.
"""

import os
import random

lista_imm = os.listdir("immagini")
print(lista_imm)

n_imm = random.randint(0, len(lista_imm) - 1)
print('Il numero estratto è: {}'.format(n_imm))
print('Nome file: {}'.format("immagini/" + lista_imm[n_imm]))
