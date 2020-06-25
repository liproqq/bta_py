# Aufgabe 1:

# Erstelle eine Funktion, welche eine musicDB erstellt.
# Sie soll eine Tabelle enthalten: 'albums'
# Die Tabelle 'albums' soll folgende Spalten enthalten:
# 'artist', 'name', year



# Aufgabe 2:
# Erstelle eine Funktion, welche einen Datensatz in die Tabelle 'albums' einfügt:

# insertAlbum(artist, albumname, year)



# Aufgabe 3:

# Erstelle zwei Suchfunktionen:
# 1. Gib alle Alben eines Artisten aus
# 2. Gib alle Alben eines Jahres aus

import sqlite3

db_name = "musicDB.db"

def createMusicDB():
    con = sqlite3.connect(db_name)
    c = con.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS albums 
                (artist TEXT, name TEXT, year INT)""")

    con.commit()
    c.close()
    con.close()

def insertAlbum(artist, name, year):

    con = sqlite3.connect(db_name)
    c = con.cursor()

    c.execute("""INSERT INTO albums VALUES (?,?,?)""", (artist, name, year))

    con.commit()
    c.close()
    con.close()


def lookup(query):

    con = sqlite3.connect(db_name)
    c = con.cursor()

    c.execute("""SELECT * FROM albums WHERE year = ? OR name = ? """, (query, query))

    result = c.fetchone()

    c.close()
    con.close()

    return result

def updateArtist(old_artist, new_artist):
    
    con = sqlite3.connect(db_name)
    c = con.cursor()


    c.execute("""UPDATE albums SET artist = ? WHERE artist = ? """, (new_artist, old_artist))

    con.commit()
    c.close()
    con.close()

def deleteAlbum(artist="", name="", year=0):
    
    con = sqlite3.connect(db_name)
    c = con.cursor()

    c.execute("""DELETE FROM albums WHERE 
                 artist = ? OR
                 name = ? OR
                 year = ? """,
                 (artist, name, year))

    con.commit()
    c.close()
    con.close()


if __name__ == "__main__":
    createMusicDB()
    insertAlbum("Limp Bizkit", "chocolate starfish and the hotdog flavored water", 2000)
    insertAlbum("Lincoln Park", "Hybrid theory", 2000)
    insertAlbum("Papa Roach", "Infest", 2000)
    insertAlbum("DMX","It's Dark and Hell Is Hot", 1998)
    print("lookup('chocolate starfish and the hotdog flavored water')",lookup("chocolate starfish and the hotdog flavored water"))
    print("lookup(2000)", lookup(2000))
    updateArtist("Lincoln Park", "Linkin Park")
    deleteAlbum(year=2000)

    