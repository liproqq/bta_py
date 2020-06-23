import sys
import os

from pathlib import Path


# gibt den absoluten Pfad zum Ordner der ausgeführten Datei
print("sys.path[0]: ", sys.path[0])
print("os.getcwd()", os.getcwd())
print()

# gibt den relativen Pfad zum Ordner der ausgeführten Datei
print("os.path.curdir: ", os.path.curdir)
# umwandeln von relativen zu absoluten Pfad
print("os.path.abspath(os.path.curdir): ", os.path.abspath(os.path.curdir))
print()

# übergeordneter Ordner
print("os.pardir: ", os.pardir)
print("os.path.abspath(os.path.pardir): ", os.path.abspath(os.path.pardir))
print()

path = sys.path[0]

# Testen ob der Pfad existiert (Datei, Ordner)
print(os.path.exists(path))
# Testen ob Pfad zu einem Ordner führt
print(os.path.isdir(path))
# Testen ob Pfad zu einer Datei führt
print(os.path.isfile(path))

print()
# zusammenfügen von Pfaden
path_file = os.path.join(path, 'dozent_dateien.py')
print(path_file)
print(os.path.isfile(path_file))
print()

# zusammenfügen eines Pfades vom C Laufwerk aus
# os.sep - seperator im Betriebssystem
path_python = os.path.join('C:', os.sep, 'python38', 'doc', 'python383.chm')
print(path_python)
print(os.path.isfile(path_python))
print()

path_python = os.path.join('C:', os.sep, 'python38')

# Path kommt von pathlib
path = Path(path_python)
print(path)

# relativer Pfad vom derzeitigen Ordner mit pathlib
path2 = Path('.').absolute()

# pathlib methoden:
# absoluter Pfad
print(path.absolute())
# relativer Pfad (zu dem Pfad in dem die Datei liegt)
print(path.relative_to(path.parent))
# Pfad existiert:
print(path.exists())
# Pfad ist Ordner
print(path.is_dir())
# Pfad ist Datei
print(path.is_file())
print()

# ausgabe von allem, was im Ordner von path ist:
for x in path.iterdir():
    print(x)
