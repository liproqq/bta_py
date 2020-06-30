import sqlite3 as sql
import pickle as pkl
from pathlib import Path
import os

data_folder = Path(__file__).parent.parent

file_to_open = data_folder / "people.pkl"

os.unlink(data_folder / "test.db")

class Fields_DB():
    def __init__(self, db_name):
        people = open(file_to_open,"rb")
        people = pkl.load(people)

        self.db_name = db_name+".db"
        self.people = people
        self.initDB()

    def initDB(self):
        con = sql.connect(self.db_name)
        con.execute("PRAGMA foreign_keys = ON")
        c = con.cursor()

        c.execute("""
              CREATE TABLE IF NOT EXISTS Fields(
              field_id INTEGER PRIMARY KEY,
              field TEXT UNIQUE)
              """)
        
        c.execute(""" 
              CREATE TABLE IF NOT EXISTS People(
              person_id INTEGER PRIMARY KEY,
              field_id INTEGER,
              Name TEXT,
              FOREIGN KEY (field_id) 
              REFERENCES field (field_id)
              )""")
        for key, people_list in self.people.items():
            try:
                c.execute(""" INSERT INTO Fields(field) VALUES (?)""", (key,))
                print(f"Field: {key} inserted")
            except Exception as e:
                    print(e)
            # self.insertField(key) Error in insertField(philosophie: database is locked)
            
            
            for person in people_list:
                c.execute("SELECT field_id FROM Fields WHERE field = ?",(key,))
                try:
                    field_id = c.fetchone()[0]
                    c.execute("INSERT INTO People(field_id, Name) VALUES (?,?)",(field_id,person))
                    print(f"Person: {person} inserted")
                except Exception as e:
                    print(f"Error when inserting person {person}: {e}")

        con.commit()
        c.close()
        con.close()


    def insertField(self, field):
        con = sql.connect(self.db_name)
        c = con.cursor()

        try:
            c.execute(""" INSERT INTO Fields(field) VALUES (?)""", (field,))
            print(f"Field: {field} inserted")
        except Exception as e:
            print(f"Error in insertField({field}: {e})")

        con.commit()
        c.close()
        con.close()
        
    
    def insertPerson(self, person, field_id):
        con = sql.connect(self.db_name)
        c = con.cursor()

        try:
            c.execute(""" INSERT INTO People(field_id, Name) VALUES (?,?)""", (field_id, person))
            print(f"Person {person} with field_id {field_id} inserted")
        except Exception as e:
            print(f"Error in insertField({field}: {e})")

        con.commit()
        c.close()
        con.close()

    def getPeople(self, field):
        listOfPeople = []
        con = sql.connect(self.db_name)
        c = con.cursor()

        c.execute("SELECT field_id FROM Fields WHERE field = ?",(field,))
        try:
            field_id = c.fetchone()[0]
            c.execute("SELECT Name FROM People WHERE field_id = (?)",(field_id,))
            listOfPeople = [person[0] for person in c.fetchall()]
        except Exception as e:
            print(f"Error getPeople ({field}): {e}")

        c.close()
        con.close()
        return listOfPeople

    def getField(self, person):
        field = ""
        con = sql.connect(self.db_name)
        c = con.cursor()

        c.execute("SELECT field_id FROM People WHERE Name = ?",(person,))
        try:
            field_id = c.fetchone()[0]
            c.execute("SELECT Field FROM Fields WHERE field_id = (?)",(field_id,))
            field = c.fetchone()[0]
        except Exception as e:
            print(f"Error getPeople ({field}): {e}")

        c.close()
        con.close()
        return field

    def changeField(self, person, field_id):
        con = sql.connect(self.db_name)
        c = con.cursor()

        try:
            c.execute("UPDATE People SET field_id = ? WHERE Name = ?",(field_id, person))            
        except Exception as e:
            print(f"Error changeField ({person}, {field_id}): {e}")
        con.commit()
        c.close()
        con.close()
        

    def deleteField(self, field):
        con = sql.connect(self.db_name)
        c = con.cursor()

        c.execute("SELECT field_id FROM Fields WHERE field = ?",(field,))
        try:
            field_id = c.fetchone()[0]
            c.execute("DELETE FROM Fields WHERE field_id = (?)",(field_id,))
            c.execute("DELETE FROM People WHERE field_id = (?)",(field_id,))
        except Exception as e:
            print(f"Error deleteField ({field}): {e}")
        con.commit()
        c.close()
        con.close()