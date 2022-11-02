import sqlite3
import sys
def dbEntry():
    # should returns correct name of database
    db = sys.argv[1]
    conn = sqlite3.connect('./' + db)
    return conn
