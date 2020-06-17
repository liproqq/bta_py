# Aufgabe 2:
# 1)
# Gib die Zahlen von 42 - 54 aus. (Inklusive 42 und 54.)
# 2)
# Gib nur die geraden Zahlen aus.
# 3) 
# Gib nur die ungeraden Zahlen aus.
#
# Bonus: 
#
# B1) Nutze eine for-Schleife und die range() Funktion.
#
# B2) Nutze eine for-Schleife, die range() Funktion und if-Anweisungen.
#
# B3) Nutze eine while-Schleife und if-Anweisungen.

print("1)")
for zahl in range(42, 55):
    print(zahl, end=", ")

print("\n\n2)")
for zahl in range(42, 55):
    if zahl % 2 == 0:
        print(zahl, end=", ")

print("\n\n3)")
for zahl in range(42, 55):
    if zahl % 2 != 0:
        print(zahl, end=", ")
