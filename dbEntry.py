import sqlite3
import sys
def dbEntry():
    # should returns correct name of database
    try:
        db = sys.argv[1]
    except: 
        db = input("Input the name of the database to be used: ")
    conn = sqlite3.connect('./' + db)
    return conn
