class Fahrzeug:
# __init__ wird beim Erzeugen des Objekts aufgerufen und setzt
# die Attribute, self ist immer das konkrete Objekt
    def __init__(self, x):
        self.geschwindigkeit = x
    def beschleunigen(self, x):
        self.geschwindigkeit += x
    # Liefert einen String, welcher das Objekt repräsentiert, wird das
    # Objekt mit der print() Methode ausgegeben, wird diese Methode
    # aufgerufen
    def __str__(self):
        return str(self.__class__)
