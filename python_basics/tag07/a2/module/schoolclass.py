class Schoolclass():

    def __init__(self, name, grades=[], year=None):
        self.name, self.grades, self.year = name, grades, year

    def add_pupil(self, pupil):
        self.pupils += pupil

    def mean_grades(self, grades):
        return sum(grades) / len(grades)

    def __str__(self):
        return "String"
