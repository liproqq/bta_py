class Car():
    def __init__(self, brand="Tesla", color="red"):
        self.brand, self.color = brand, color
    

    def change_col(self, color):
        self.color = color

    def __str_(self):
        return f"Brand: {self.brand}\n Color: {self.color}"
