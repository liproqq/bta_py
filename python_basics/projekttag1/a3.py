# Schreibe eine Funktion, die testet ob eine übergebene Zahl eine Primzahl ist.
# Primzahlen sind nur durch 1 und sich selbst teilbar. (1 selbst ist keine Primzahl.)

import random


def primzahl(x):
    primzahlen = [2, 3]
    for potentiellePrimzahl in range(3, x+1):
        teilbar = list(filter(lambda primzahl: potentiellePrimzahl % primzahl == 0, primzahlen))
        # todo: exit wenn teilbar auftaucht
        # if len(teilbar): return False
        if not len(teilbar) and x == potentiellePrimzahl:
            return True
        if not len(teilbar):
            primzahlen.append(potentiellePrimzahl)
    return False


# Alternative
def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


for n in range(10):
    test = random.randint(10, 20)
    print(f"{test} {primzahl(test)}")


for n in range(10, 20):
    if isPrime(n):
        print(f"{n} ist eine Primzahl")
    else:
        print(f"{n} ist keine Primzahl")
