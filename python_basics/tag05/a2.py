# Aufgabe 2
# Umrechnungen
#
# Erstelle zwei Funktionen.
# Eine, welche Gramm in Kilogramm umrechnet.
# Eine, welche Kilogramm in Gramm umrechnet.
#
#
#
# kg = g_2_kg(g)
# g = kg_2_g(kg)
#
#
#
# 1kg == 1000g
#
#
#
# Bonus:
# Schreibe eine Funktion, welche eine Zahl und einen String ('kg' oder 'g') übergeben bekommt und dann in die jeweils andere Größe umwandelt.
#
#
#
# change = change_weight(x, orig)
# orig = Ursprungsgröße ('kg' oder 'g')
# x = ist der Zahlenwert der Ursprungsgröße

def g_2_kg(g):
    return g/1000


def kg_2_g(kg):
    return kg*1000


def change_weight(x, orig):
    if(orig == "kg"):
        return f"{kg_2_g(x)} g"
    if(orig == "g"):
        return f"{g_2_kg(x)} kg"
    print(f"Fehler: {orig} wird nicht unterstützt")


print(change_weight(float(input("Gewicht eingeben(ohne Einheit): ")),
                          input("Einheit(g oder kg): ")))
