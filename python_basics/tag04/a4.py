# Aufgabe 4:
#
# Erstelle die folgenden Ausgaben Automatisch:
#
# 0 0 0 0
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
#
# 0 1 2 3
# 0 1 2 3
# 0 1 2 3
# 0 1 2 3
#
# Bonus: Erstelle es so, daß eine beliebige Zeilen
# und Spalten zahl eingegeben werden kann.

reihen = int(input("Reihen: "))
spalten = int(input("Spalten: "))

tabelle = []

# for i in range(spalten):
#     spalte = []
#     for j in range(reihen):
#         spalte.append(j)
#     tabelle.append(spalte)
#
# print(tabelle)

for i in range(spalten):
    for j in range(reihen):
        print(j, end=" ")
    print()

print()
print()
for i in range(spalten):
    for j in range(reihen):
        print(i, end=" ")
    print()
