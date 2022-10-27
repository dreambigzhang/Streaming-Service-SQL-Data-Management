import sqlite3
import time
from pprint import pprint
import getpass

connection = None
cursor = None

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return

    
def main():
    global connection, cursor

    # connect to db (need to take input?)
    path = "./a2.db"
    connect(path)
    
    enterType = 0  # 1 = login ... 2 = sign up
    while enterType != 1 and enterType != 2: 
        enterType = input("Type 1 to login or 2 to sign up")

    # LOGIN portion NEED TO SPLIT INTO FUNCTIONS
    validUser = False  # true if gives rowcount > 0
    ValidArtist = False
    
    if enterType == 1:
        # keep asking for id and password till correct, how should we add option to back out? 
        while not validUser or not validArtist: 

            ID = input("Enter ID: ")
            pwd = getpass.getpass(prompt='Enter your password: ', stream= None)

            validUser = False
            validArtist = False
            
            #check if valid user
            cursor.execute('''
                SELECT u.uid 
                FROM users u
                WHERE uid = ? and pwd = ?'''
                ,(ID,pwd))

            if cursor.rowcount() != 0:
                userID = cursor.fetchone()
                validUser = True
        
            #check if valid artist
            cursor.execute('''
                SELECT a.aid 
                FROM artists  
                WHERE uid = ? and pwd = ?'''
                ,(ID,pwd))

            if cursor.rowcount() != 0:
                artistID = cursor.fetchone()
                validArtist = True
    else if enterType == 2:
        validNewID = 0
        while validNewID == 0: 
            
            userID = input("Input a unique ID: ")
            # check if unique ID
            cursor.execute('''
                SELECT uid
                FROM users  
                WHERE uid = ?'''
                ,(userID))
            validNewID = cursor.rowcount()
            if validNewID == 0: 
                print("ID is not unique")
                
        userPWD = input("Input a new password")
        cursor.execute("""INSERT INTO users VALUE (?,?)""",(userID,userPWD))
    
    




    connection.commit()
    connection.close()
    return


if __name__ == "__main__":
    main()
