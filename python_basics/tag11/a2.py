import sqlite3

def createDBs():
    con = sqlite3.connect("country.db")
    con.execute("PRAGMA FOREIGN_KEYS = ON")

    c = con.cursor()

    c.execute("""
              CREATE TABLE IF NOT EXISTS countries(
              country_id INTEGER PRIMARY KEY UNIQUE,
              country TEXT UNIQUE,
              pop INTEGER)
              """)
    

    c.execute(""" 
              CREATE TABLE IF NOT EXISTS cities(
              city_id INTEGER PRIMARY KEY,
              city text,
              pop INTEGER,
              country_id INTEGER,
              FOREIGN KEY (country_id) 
              REFERENCES countries (country_id)
              )""")

    con.commit()
    c.close()
    con.close()

def insertCountry(country, pop):
    con = sqlite3.connect("country.db")
    con.execute("PRAGMA FOREIGN_KEYS = ON")
    c = con.cursor()

    try:
        c.execute("INSERT INTO countries (country,pop) VALUES (?,?) ;", (country,pop))
        con.commit()
    except Exception as e:
        print(f"insertCountry Error: {e}")

    c.close()
    con.close()

def insertCity(city_name, pop, country_name):
    con = sqlite3.connect("country.db")
    con.execute("PRAGMA FOREIGN_KEYS = ON")
    c = con.cursor()

    c.execute("SELECT country_id FROM countries WHERE country = ?", (country_name,))


    try:
        country_id = c.fetchone()[0]
        c.execute("INSERT INTO cities (city, pop, country_id) VALUES (?,?,?) ;", (city_name, pop, country_id))
        con.commit()
    except Exception as e:
        print(e)

    c.close()
    con.close()
    
def searchCitysCountry(city):
    result = []

    con = sqlite3.connect("country.db")
    c = con.cursor()

    c.execute("SELECT country_id FROM cities WHERE city = ?", (city,))

    country_ids = c.fetchall()

    for id in country_ids:
        c.execute("SELECT country FROM countries WHERE country_id = ?", (id[0],))
        result.append(c.fetchone()[0])
    return result
        


if __name__ == "__main__":
    createDBs()
    insertCountry("Chile",533)
    insertCountry("Pakistan",1333)
    insertCity("Santiago", 200, "Chile")
    insertCity("Santiago", 200, "Kolumbien")
    print(searchCitysCountry("Santiago"))