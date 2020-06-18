class Animal():
    """docstring for animal."""

    def __init__(self, lebendauer, gewicht):
        self.__lebensdauer, self.__gewicht = lebendauer, gewicht

    def get_lebensdauer(self):
        return self.__lebensdauer

    def set_lebensdauer(self, lebensdauer):
        self.__lebensdauer = lebensdauer

    def get_gewicht(self):
        return self.__lebensdauer

    def set_gewicht(self, gewicht):
        self.__gewicht = gewicht

    def __str__(self):
        return f"Lebensdauer: {self.get_lebensdauer()}\nGewicht: {self.get_gewicht()}"


if __name__ == '__main__':
    hund = Animal(10, 15)
    katze = Animal(7, 5)

    print(hund, katze)
