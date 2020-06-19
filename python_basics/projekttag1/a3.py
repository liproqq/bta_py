# Schreibe eine Funktion, die testet ob eine übergebene Zahl eine Primzahl ist.
# Primzahlen sind nur durch 1 und sich selbst teilbar. (1 selbst ist keine Primzahl.)

import random


def primzahl(x):
    primzahlen = [2, 3]
    for zahl in range(3, x+1):
        teilbar = list(filter(lambda primzahl: zahl % primzahl == 0, primzahlen))
        if not len(teilbar) and x == zahl:
            return True
        if not len(teilbar):
            primzahlen.append(zahl)
    return False


for n in range(10):
    test = random.randint(1000, 2000)
    print(f"{test} {primzahl(test)}")
