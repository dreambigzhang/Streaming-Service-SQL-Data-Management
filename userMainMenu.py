
import sqlite3
from startSession import startSession
from endSession import endSession
from searchSongsAndPlaylists import searchSongsAndPlaylists
from searchArtists import searchArtists
conn = sqlite3.connect('./a2.db')

from os import system, name

def clear(): # need to test this works on lab machine
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def userMainMenu(uid, conn):
    c = conn.cursor()
    clear()
    print("------User Main Menu-------")
    action = input("Enter\n1 to start session\n2 to end session\n3 to search for songs and playlists\n4 to search for artists\nAnything else to logout\n")
    if action=='1':
        clear()
        startSession(uid, conn)
        userMainMenu(uid, conn)
    elif action == '2':
        clear()
        endSession(uid, conn)
        userMainMenu(uid, conn)
    elif action == '3':
        clear()
        if searchSongsAndPlaylists(uid, conn)==True:
            userMainMenu(uid, conn)
    elif action == '4':
        clear()
        if searchArtists(uid, conn)== True:
            userMainMenu(uid, conn)
    else:
        print("logout")

userMainMenu('u1', conn)