# Aufgabe 4:
# FloatTest
#
# Schreibe eine Funktion, welche einen String als Eingabe bekommt.
# Sie soll prüfen ob der String in eine Fließkommazahl umgewandelt werden kann.
# Wenn ja, soll die Funktion True zurück geben, wenn nein False.
#
# isFloat(zahl) (Funktion)
# zahl = str (Zeichenkette/String)

def isFloat(string):
    try:
        float(string)
        return True
    except Exception:
        return False


zahl = input("Bitte Float eingeben: ")
print(isFloat(zahl))
