from modules.fields_db import Fields_DB
from pathlib import Path

db = Fields_DB("test")

db.insertField("data science")
db.insertPerson("Manuel", 4)
print(db.getPeople("math"))
print(db.getField("Platon"))
db.changeField("Sokrates", 1)
print(db.getField("Sokrates"))
db.deleteField("physics")