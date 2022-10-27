import sqlite3
import getpass

conn = sqlite3.connect('./a2.db')

c = conn.cursor()

def login(): # returns userID and artistID, at least one is not None
    userID = None
    artistID = None
    while userID == None and artistID == None: 
            #take ID and password
            ID = input("Enter ID: ")
            pwd = getpass.getpass(prompt='Enter your password: ', stream= None)
            
            #check if valid user
            c.execute('''
                SELECT u.uid 
                FROM users u
                WHERE uid = ? and pwd = ?;'''
                ,(ID,pwd))
            
            row = c.fetchone()
            if c.rowcount() != 0:
                userID = row[0]
        
            #check if valid artist
            c.execute('''
                SELECT a.aid 
                FROM artists  
                WHERE uid = ? and pwd = ?;'''
                ,(ID,pwd))
            
            row = c.fetchone()
            if c.rowcount() != 0:
                artistID = row[0]
            if userId == None and artistId == None:
                print("Not a valid username or password")
    return userID, artistID
                

