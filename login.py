import sqlite3
import getpass

conn = sqlite3.connect('./a2.db')

c = conn.cursor()

def login(): 
    validUser = False
    validArtist = False
    while not validUser or not validArtist: 
            #take ID and password
            ID = input("Enter ID: ")
            pwd = getpass.getpass(prompt='Enter your password: ', stream= None)
            
            #check if valid user
            c.execute('''
                SELECT u.uid 
                FROM users u
                WHERE uid = ? and pwd = ?'''
                ,(ID,pwd))
            
            row = c.fetchone()
            if c.rowcount() != 0:
                userID = row[0]
                validUser = True
        
            #check if valid artist
            c.execute('''
                SELECT a.aid 
                FROM artists  
                WHERE uid = ? and pwd = ?'''
                ,(ID,pwd))
            
            row = c.fetchone()
            if c.rowcount() != 0:
                artistID = row[0]
                validArtist = True
            if not validUser and not validArtist:
                print("Not a valid username or password")
    return validUser, ValidArtist
                

