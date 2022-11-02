import sqlite3
import getpass

def login(conn): # returns userID and artistID, at least one is not None
    c = conn.cursor()
    
    userID = None
    artistID = None
    back = False
    while userID == None and artistID == None and back == False: 
            #take ID and password
            
            ID = input("Enter ID or input -1 to go back: ").lower()  # userID and artistID will be None
            if ID.strip() == '-1':
                break
            pwd = getpass.getpass(prompt='Enter your password: ', stream= None)
            
            # query all users matching ID and pwd
            c.execute('''
                SELECT u.uid 
                FROM users u
                WHERE lower(u.uid) = ? and u.pwd = ?;'''
                ,(ID,pwd))
            
            # check if valid user ID
            row = c.fetchone()
            if row is not None:
                userID = row[0]
        
            # query all artists matching ID and pwd
            c.execute('''
                SELECT a.aid 
                FROM artists a 
                WHERE lower(a.aid) = ? and a.pwd = ?;'''
                ,(ID,pwd))
            
            # check if valid user ID
            row = c.fetchone()
            if row is not None:
                artistID = row[0]
            
            # if incorrect ID and pwd tell user and redo loop
            if userID == None and artistID == None:
                print("Not a valid username or password")
    return userID, artistID  # if both are none then user is backing out
               
