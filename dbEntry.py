import sqlite3

def dbEntry():
    # should returns correct name of database
    db = input("Input name of database file")
    conn = sqlite3.connect('./' + db)
    return conn
