# Lies eine Zahl zwischen 1582 und 2020 ein.
# Oder lasse zufällig eine Zahl erstellen mit dem random Modul:
# import random
# zufallszahl = random.randint(1582, 2020)
# Überprüfe, ob diese Zahl einem Schaltjahr entspricht.
# Ein Schaltjahr ist alle vier Jahre.
# Alle 100 Jahre ist jedoch kein Schaltjahr.
# Alle 400 Jahre wird diese Regel aber durchbrochen und das Schaltjahr findet statt.
# Die Jahre 1700, 1800, 1900, wie auch 2100 sind keine Schaltjahre. Die Jahreszahl ist
# zwar durch vier teilbar, aber ebenso durch 100, nicht aber durch 400. Das Jahr 2000 war
# ein Schaltjahr - es ist durch 4, durch 100, wie auch durch 400 ganzzahlig teilbar.
# Siehe auch:
# https://de.wikipedia.org/wiki/Schaltjahr


import random
zufallszahl = random.randint(1582, 2020)


def Schaltjahr(jahr):
    ergebnis = False
    if jahr % 400 == 0:
        ergebnis = True
        print("Durch 400 teilbar")
    if jahr % 4 == 0 and jahr % 100 != 0:
        ergebnis = True
        print("Durch 4 teilbar und nicht durch 100")
    return ergebnis


for n in range(50):
    zufallszahl = random.randint(1582, 2020)
    print(f"{zufallszahl} {Schaltjahr(zufallszahl)}")

print(f"2000 {Schaltjahr(2000)}")
print(f"1600 {Schaltjahr(1600)}")
