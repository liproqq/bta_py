# Erstelle ein Programm, welches die Zahlen von 1 - 10.
# In die jeweilige Zeile schreibt.

# Bonus: Erstelle die Aufgabe als Funktion, welche eine
# beliebige Zeilenanzahl übergeben bekommt.

from pathlib import Path


data_folder = Path("python_basics/tag09/")

file_to_open = data_folder / "new.txt"

f = open(file_to_open,"w")

def printListOfNumbersToFile(x):
    print(f"creating list of {x} Numbers in {file_to_open}")
    for i in range(1, x+1):
        f.write(f"{i}\n")
    print("finished")


printListOfNumbersToFile(10)
