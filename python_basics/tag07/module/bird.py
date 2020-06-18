from module.animal import Animal

class Bird(Animal):
    """docstring for Bird."""

    def __init__(self, lebendauer, gewicht, eggColor, eggSize):
        super().__init__(lebendauer, gewicht)
        self.eggColor, self.eggSize = eggColor, eggSize

    def __str__(self):
        return f"Lebensdauer: {self.get_lebensdauer()}\nGewicht: {self.get_gewicht()}\nEierfarbe: {self.eggColor}\nEiergröße: {self.eggSize}"
