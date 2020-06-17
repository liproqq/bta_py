# Aufgabe 3
#
# Lies eine Zahl ein.
#
# Überprüfe ob diese Zahl in der Liste vorhanden ist. (Mit if, else)
zahl_input = int(input("Bitte Zahl eingeben: "))

zahlen = [1, 3, 5, 1, 9, 8, 6]

if zahl_input in zahlen:
    print(f"Die Zahl {zahl_input} ist vorhanden")
else:
    print(f"Die Zahl {zahl_input} ist nicht vorhanden")
