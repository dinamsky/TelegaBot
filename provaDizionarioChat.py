""" Creazione ed uso di dizionario Chat ID.
Si usa per avere un archivio di flag per ogni chat che dialoga con il Bot.
"""
ChatID = {-2861403: False, 163078549: True, 345: False, 123: False, 789: True}
print(ChatID)

singoloID = 765

# Prima il controllo che esista, quindi quello che verrà fatto in start. Se non esiste dovrebbe appendere il nuovo numero e impostarlo su True:
if not(singoloID in ChatID.keys()):
    ChatID[singoloID] = True

# Poi la modifica che verrà fatta in stop, ovvero impostare su False:
ChatID[singoloID] = False
print(ChatID)

# E infine quello che viene fatto nei filtri, ovvero il ritorno dello stato
return ChatID[singoloID]
