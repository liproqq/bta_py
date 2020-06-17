# Aufgabe 3:
# Pseudo-Range (abgeändert)
#
# Erstelle eine Funktion, welche zwei Zahlen übergeben bekommt.
# Sie soll eine Liste mit allen ganzen Zahlen zwischen den zwei Zahlen erstellen.
# (Inclusive Start und Ende. Start soll kleiner als Ende sein.)
#
#
#
# Variablen: 
# numlist = pseudoRange(start, ende) (Funktion)
# start = int (Integer/ ganze Zahl)
# ende = int (Integer/ ganze Zahl)
# numlist = list (Liste)
#
#
# Bonus:
# Wenn Ende größer als Start ist soll immer eine Liste von der kleineren
# zur größeren Zahl erstellt und zurückgegeben werden.

def pseudoRange(start, ende):
    if ende < start:
        return list(range(ende, start + 1))
    return list(range(start, ende+1))


numlist = pseudoRange(
            int(input("Bitte Anfang der Liste angeben: ")),
            int(input("Bitte Ende der Liste angeben: "))
            )

print(numlist)
