# Aufgabe: 
#
# Lies beliebig viele Zahlen ein.
# Höre auf, sobald eine Zahl negativ ist.
#
# Bonus: Speichere alle Zahlen in einer Liste.

zahlen = []

while True:
    zahl = int(input("Bitte Zahl eingeben: "))
    if zahl >= 0:
        zahlen.append(zahl)
        print(zahl*zahl)
    else:
        break

print(zahlen)
