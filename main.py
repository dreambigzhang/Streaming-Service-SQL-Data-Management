import sqlite3
from dbEntry import dbEntry
from loginOrSign import loginOrSign
from login import login
from signup import signup
from userMainMenu import userMainMenu
conn = dbEntry()

def main(): 
      # returns name of database

    initialAction = loginOrSign() # 1 for login, 2 for sign up, all else for exit
    uid = None 
    aid = None
    if initialAction == '1':
        uid,aid = login(conn)  # if both stay None, user is backing out to loginOrSign function again
    elif initialAction == '2': 
        uid = signup(conn) # signing up user
    else: 
        return  # exit program

    if uid == None and aid == None:  # means to back out to main screen again
        main() 
        return
    elif uid == aid: 
        action = input("Enter 1 to go into your user account or 2 to enter into your artist account: ").strip()
        while action != '1' and action != '2': 
            print("Invalid action, try again")
            action = input("Enter 1 to go into your user account or 2 to enter into your artist account: ").strip()
        
        if action == '1': 
            possibleLogout = userMainMenu(uid,conn) # userMainMenu returns 5 if logout, returns None otherwise
            if possibleLogout == '5': 
                main()
                return
        else: 
            # put artist main menu here
            return
    elif uid != None: 
        possibleLogout = userMainMenu(uid,conn)
        if possibleLogout == '5':
            main()
            return
    else: 
        # put artist main menu here
        return
    

main()
