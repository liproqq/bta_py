from classes.car import Car
import pickle
from pathlib import Path

data_folder = Path("python_basics/tag09/")

file_to_open = data_folder / "cars.pkl"

f = open(file_to_open,"wb")

new_car1 = Car()
new_car2 = Car("Toyota", "silver")

pickle.dump(new_car1, f)
pickle.dump(new_car2, f)

f.close()

