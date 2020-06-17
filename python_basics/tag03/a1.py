# Aufgabe 1
# 1 Erstelle ein Dictionary welches Namen speichert.
#   Die Nachnamen sollen als Key dienen und die Vornamen als Value.
# 2 Gib alle Vornamen aus.
# 3 Gib alle Nachnamen aus.
# 4 Gib alle Namen gesamt aus.
# Bonus Gib die Namen in der Form: Vorname: {vorname}, Nachname: {nachname} aus

names = {
    "Brenner": "Claudia",
    "Chlor": "Peter",
    "Dreher": "Bernadette",
    "Elstner": "Frank"
}

print(names.values())
print(names.keys())
print(names.values(), names.keys())

for name in names:
    print(f"Vorname: {names[name]}, Nachname: {name}")
