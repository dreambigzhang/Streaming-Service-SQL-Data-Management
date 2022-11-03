
import sqlite3
from startSession import startSession
from endSession import endSession
from searchSongsAndPlaylists import searchSongsAndPlaylists
from searchArtists import searchArtists


from os import system, name

def clear(): # need to test this works on lab machine
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def userMainMenu(uid, conn):
    #clear()
    print("------User Main Menu-------")
    action = input("Enter\n1 to start session\n2 to end session\n3 to search for songs and playlists\n4 to search for artists\n5 to logout\nAnything else to exit program \n").strip()
    if action=='1':
        clear()
        startSession(uid, conn)
        return userMainMenu(uid, conn)
    elif action == '2':
        clear()
        endSession(uid, conn)
        return userMainMenu(uid, conn)
    elif action == '3':
        clear()
        if searchSongsAndPlaylists(uid, conn)==True:
            return userMainMenu(uid, conn)
    elif action == '4':
        clear()
        if searchArtists(uid, conn)== True:
            return userMainMenu(uid, conn)
    elif action == '5':
        endSession(uid, conn)
        clear()
        print("logged out")
        return '5' # should return to main screen
    else:
        endSession(uid, conn)
        clear()
        return -1
    return

if __name__ == "__main__":
    conn = sqlite3.connect('./new.db')
    userMainMenu('u1', conn)
