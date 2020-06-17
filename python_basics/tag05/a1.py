# Erstelle ein Programm, welches beliebige Grad-Celsius
# Eingaben in Kelvin umrechnet.
# Lies dazu eine Celsius Zahl ein und nutze eine Funktion zum
# Berechnen des Kelvin Wertes.
#
# 1 C = 274,15 K
#
# Variablen:
# umrechnungsfunktion: c_in_k(c)
# eingelesener wert: cel
# ausgegebener wert: kev
#
# Bonus: gib alle Kelvin Werte aus für die Ganzzahligen
# Celsius Werte von 0 - 25

def c_in_k(c):
    return c+273.15


cel = float(input("Bitte Celsius eingeben: "))
print(c_in_k(cel))

print("----------------------------------")

for i in range(26):
    print(c_in_k(i))
