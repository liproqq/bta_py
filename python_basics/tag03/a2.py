# Aufgabe 2
# Lies ein Wort ein.
# Teste ob es eines der folgenden Wörter ist und gib den gegebenen Satz aus:
# (Nutze if Bedingungen)
#     'Hund': 'Der Hund macht Wau!'
#     'Katze': 'Die Katze macht Miau!'
#     'Maus': 'Die Maus macht Piep!'
# Wenn es keines der Wörter ist gib aus:
#     'Unbekanntes Tier'

tier_input = input("Bitte ein Tier eingeben:")

tiere = {'Hund': 'Der Hund macht Wau!',
         'Katze': 'Die Katze macht Miau!',
         'Maus': 'Die Maus macht Piep!'
         }

if tier_input in tiere:
    print(tiere[tier_input])
else:
    print('Unbekanntes Tier')
