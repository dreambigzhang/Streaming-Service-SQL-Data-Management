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
            
            # query all users matching ID and pwd
            c.execute('''
                SELECT u.uid 
                FROM users u
                WHERE u.uid = ? and u.pwd = ?;'''
                ,(ID,pwd))
            
            # check if valid user ID
            row = c.fetchone()
            if row is not None:
                userID = row[0]
        
            # query all artists matching ID and pwd
            c.execute('''
                SELECT a.aid 
                FROM artists a 
                WHERE a.aid = ? and a.pwd = ?;'''
                ,(ID,pwd))
            
            # check if valid user ID
            row = c.fetchone()
            if row is not None:
                artistID = row[0]
            
            # if incorrect ID and pwd tell user and redo loop
            if userID == None and artistID == None:
                print("Not a valid username or password")
    return userID, artistID
               