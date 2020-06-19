# Schreibe eine Funktion, welche den euklidischen Abstand zwischen zwei Punkten
# Berechnet. Jeder Punkt besteht aus Koordinaten.
# 1) Der Abstand soll im 2-Dimensionalen Raum berechnet werden.
# a = (ax, ay)
# b = (bx, by)
# (Entspricht der Berechnung einer Hypotenuse nach Satz des Pythagoras.)
# für zwei Punkte a und b: √((ax−bx)^2+(ay−by )^2)
# (Wurzel: a = a**0.5)
# https://de.wikipedia.org/wiki/Satz_des_Pythagoras
# *Bonus: Die Funktion soll für alle n-Dimensionalen Räume gelten.
# a = (a1, a2, ..., an)
# b = (b1, b2, ..., bn)
# √(a1−b1)
# 2+...+(an−bn)
# 2
# https://de.wikipedia.org/wiki/Euklidischer_Abstand

def abstand2D(a=(0, 0), b=(2, 2)):
    return (((a[0]-b[0])**2) + (a[1]-b[1])**2)**0.5


a = (1, 1)
b = (1, 2)
print(f"Aufgabe 1: {abstand2D(a, b) == 1}")


def abstandND(a, b):
    if len(a) != len(b): return "Punkte haben nicht die selbe Dimension"
    sum = 0
    # reduce?
    for n in range(len(a)):
        sum += (a[n]-b[n])**2
    return sum**0.5


m = (0, 0, 0, 0, 0, 0)
n = (0, 0, 0, 0, 0, 5)

print(f"Aufgabe 2: {abstandND(m, n)}")
