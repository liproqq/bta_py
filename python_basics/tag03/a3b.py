# Aufgabe 3
#
# Lies eine Zahl ein.
# Bonus: Gib an wie oft sie vor kommt
# Überprüfe ob diese Zahl in der Liste vorhanden ist. (Mit if, else)
zahl_input = int(input("Bitte Zahl eingeben: "))

zahlen = [1, 3, 5, 1, 9, 8, 6]
counter = 0

if zahl_input in zahlen:
    for zahl in zahlen:
        if zahl_input == zahl:
            counter += 1
    print(f"Die Zahl {zahl_input} ist {counter} mal vorhanden")
else:
    print(f"Die Zahl {zahl_input} ist nicht vorhanden")
