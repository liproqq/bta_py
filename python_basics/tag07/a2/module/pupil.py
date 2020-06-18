class Pupil:
    def __init__(self, name, grades=[]):
        self.year = None
        self.name = name
        self.grades = grades

    def __str__(self):
        return f"Name: {self.name}\nKlassenstufe: {self.year}"

    def set_year(self, y):
        self.year = y

    def mean_grades(self):
        # var 1
        # return sum(self.grades) / len(self.grades)
        # var 2
        x = 0
        for grade in self.grades:
            x += grade
        m = x / len(self.grades)
        return m


if __name__ == '__main__':
    pupil1 = Pupil('Heinz', [6, 5, 4])
    pupil2 = Pupil('Helga', [2, 4, 3])

    pupil1.set_year(1)

    print(pupil1)
    print(pupil2)

    print(pupil1.mean_grades())
    print(pupil2.mean_grades())
