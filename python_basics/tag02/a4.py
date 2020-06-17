# Aufgabe 4
# Gib das Quadrat jedes Elements aus der folgenden Liste aus:
# (Nutze die for-Schleife)
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrate = []

for zahl in zahlen:
    quadrate.append(zahl*zahl)

print(quadrate)


quadrate = list(map(lambda zahl: zahl*zahl, zahlen))
print(quadrate)
