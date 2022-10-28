
import sqlite3
from scrolling import clear
from startSession import startSession
from endSession import endSession
conn = sqlite3.connect('./a2.db')


def userMainMenu(uid, conn):
    c = conn.cursor()
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
        print("search for songs and playlists")
    elif action == '4':
        print("search for artists")
    else:
        print("logout")

userMainMenu('u1', conn)