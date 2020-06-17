# Aufgabe 2:
# Klasse Konto
#
#
# Erstelle die Klasse 'Konto'.
#
# Bei der initialisierung soll die Klasse den user und die knr übergeben bekommen.
#
# Der Kontostand (betrag) soll auf 0 gesetzt werden.
#
#
#
# Die Methode abheben(x) soll den betrag um x verkleinern.
#
# Die Methode einzahlen(x) soll den betrag um x erhöhen.
#
#
#
# Überlege dir eine schöne ausgabe für deine Objekte mit __str__().
#
# Bonus:
# 1
# Stelle sicher, daß keine negativen Beträge eingezahlt werden. 
# 2
# Stelle sicher, daß der Kontostand nicht negativ wird. 
# 3
# Fange falsche eingaben ab. (z.B. 'AAA' für eingabe())

class Konto():

    def __init__(self, user, knr):
        self.user, self.knr = user, knr
        self.betrag = 0

    def abheben(self, x):
        if not self.validierung(x):
            print("Eingabe ungültig")
            return
        if x > 0 and x > self.betrag:
            print("Fehler: Zu wenig Guthaben.")
            return

        self.betrag -= x
        self.display()

    def einzahlen(self, x):
        if not self.validierung(x):
            print("Eingabe ungültig")
            return
        if x <= 0:
            print("Fehler: Ungültiger Einzahlungsbetrag")
            return

        self.betrag += x
        self.display()
        return

    def display(self):
        print(f"Neuer Kontostand: {self.betrag}")

    def validierung(self, x):
        try:
            float(x)
            return True
        except Exception:
            return False

    def __str__(self):
        return f"User: {self.user} \nKontostand: {self.betrag}"
