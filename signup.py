import sqlite3
import getpass

conn = sqlite3.connect('./a2.db')

c = conn.cursor()

def signup(): 
    userID = None
    while userID == None or len(userID) > 20: 

        userID = input("Input a unique ID: ")
        pwd = getpass.getpass(prompt='Enter your password: ', stream= None)
        # check if unique ID
        c.execute('''
            SELECT uid
            FROM users  
            WHERE uid = ?'''
            ,(userID))
        validNewID = c.rowcount()
        if validNewID == 0: 
            print("ID is not unique")
            userID = None  # while loop continues


    c.execute("""INSERT INTO users VALUE (?,?)""",(userID,userPWD))
