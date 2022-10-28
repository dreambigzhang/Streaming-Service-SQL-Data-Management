import sqlite3
import getpass

conn = sqlite3.connect('./a2.db')

c = conn.cursor()

def signup(): 
    userID = None
    while userID == None or len(userID) > 20: 

        userID = input("Input a unique ID: ")
        pwd = getpass.getpass(prompt='Enter your password: ', stream= None)
        name = input("What is your name? ")
        # check if unique ID
        c.execute('''
            SELECT u.uid
            FROM users u 
            WHERE u.uid = ?;'''
            ,(userID,))
        validNewID = c.fetchone()
        if validNewID is not None: 
            print("ID is not unique")
            userID = None  # while loop continues


    c.execute("""INSERT INTO users VALUES (?,?,?);""",(userID,name,pwd))