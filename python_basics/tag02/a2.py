# Aufgabe*:
# Schreibe ein Programm, welches den User auffordert, einen Geldbetrag (int) einzugeben.

# Jetzt soll berechnet werden, wie dieser Betrag in Scheine und Münzen zerlegt werden kann.

# (z. B. 85€: 1 x 50, 1 x 20, 1 x 10, 1 x 5)

betrag = int(input("Geldbetrag eingeben: "))

scheine = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0}


for schein in scheine:
    # Aktueller Betrag wird durch aktuelle Scheingröße geteilt
    scheine[schein] = betrag // schein
    if scheine[schein] > 0:
        print(f"{scheine[schein]} x {schein}€-Schein")

    # Aktueller BEtrag verringert sich um den Betrag, der durch den aktuellen Schein abgedeckt werden kann
    betrag = betrag - scheine[schein]*schein
    if betrag == 0:
        break
