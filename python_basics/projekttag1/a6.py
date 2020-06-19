# Erstelle eine Klasse: Verien
# Attribute: name, vorsitz, vorstand (Liste), mitglieder (Liste)
# Methoden: vorstandWaehlen(), vorsitzendenWaehlen(), mitgliedHinzufuegen(),
# mitgliedEntlassen()
# 1) Die Klasse Verein bekommt bei der Initialisierung nur den Namen zugewiesen.
# 2) mitgliedHinzufuegen(): eine Methode, die dem Verein Mitglieder hinzufügt.
# 3) vorstandWaehlen(): eine Methode, die dem Vorstand genau fünf Mitglieder zuweist.
#  durch Manuelle Zuweisung (Über die Liste mitglieder gehen) oder zufällig z.B. mit:
# import random
# 4) vorsitzendenWaehlen(): eine Methode, die ein Vorstandsmitglied zum Vorsitzenden
# random.choice(Liste)
#  macht.
# 5) mitgliedEntlassen(): eine Methode, die ein bestimmtes Mitglied aus dem Verein löscht.
#  Bonus:
#  Bei entlassen eines Vorstandsmitglieds/des Vorsitzes müssen Neuwahlen stattfinden.

import random


class Verein():
    def __init__(self, name):
        self.name = name
        self.vorsitz = ""
        self.vorstand = []
        self.vorstandsvorsitzender = ""
        self.mitglieder = []

    def mitgliedHinzufuegen(self, mitglied):
        self.mitglieder.append(mitglied)
        print(f"{mitglied} ist dem Verein begetreten")

    def vorstandWaehlen(self):
        self.vorstand = []
        while len(self.vorstand) < 5:
            vorstandskandidat = random.choice(self.mitglieder)
            if vorstandskandidat not in self.vorstand:
                self.vorstand.append(vorstandskandidat)
        self.vorsitzendenWaehlen()
        print(f"Neuer Vorstand: {self.vorstand}")

    def vorsitzendenWaehlen(self):
        vorstand = random.choice(self.vorstand)
        print(f"{vorstand} ist der neue Vorstandvorsitzende")
        self.vorstandsvorsitzender = vorstand

    def mitgliedEntlassen(self, mitglied):
        if mitglied not in self.mitglieder:
            print("Ungültiges Mitglied: Nicht im Verein")
        elif mitglied in self.vorstand:
            self.mitglieder.remove(mitglied)
            self.vorstandWaehlen()
            print(f"{mitglied} war im Vorstand und wurde entfernt")
        else:
            self.mitglieder.remove(mitglied)
            print(f"{mitglied} wurde entfernt")


if __name__ == '__main__':
    bayer04 = Verein("Bayer 04 Leverkusen")
    for i in ["Hradecky", "Tapsoba", "S: Bender", "Tah", "Sinkgraven",
              "Aranguiz", "Demirbay", "Weiser", "Bailey", "Havertz", "Bellarabi"
              ]:
        bayer04.mitgliedHinzufuegen(i)
    bayer04.vorstandWaehlen()
    bayer04.mitgliedEntlassen("Weiser")
