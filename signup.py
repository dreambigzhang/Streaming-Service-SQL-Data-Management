import sqlite3
import getpass

def signup(conn): 
    c = conn.cursor()
    
    userID = None
    while userID == None or len(userID) > 20: 
            
        userID = input("Input a unique ID of size 4 or less, or input -1 to go back: ").lower()
        if userID == '-1':
            return
        while len(userID) > 4: 
            print("The ID is too large, try again")
            userID = input("Input a unique ID of size 4 or less: ")
        pwd = getpass.getpass(prompt='Enter your password: ', stream= None)
        name = input("What is your name? ")
        # check if unique ID
        c.execute('''
            SELECT u.uid
            FROM users u 
            WHERE lower(u.uid) = ?;'''
            ,(userID,))
        validNewID = c.fetchone()
        if validNewID is not None: 
            print("ID is not unique")
            userID = None  # while loop continues


    c.execute("""INSERT INTO users VALUES (?,?,?);""",(userID,name,pwd))
    conn.commit()
    return userID  # to start doing user actions instantly