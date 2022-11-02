import sqlite3
from os import system, name
from songActions import songActions

def clear(): # need to test this works on lab machine
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
 
def showFive(list1, i):
    listLen = len(list1)
    if listLen == 0:
        i = 0
    else:
        i = i % listLen
    
    clear()
    j = i
    print("--- Artist Search Result---")
    print("  id |   name   | nationality | duration of all songs")
    while j<i+5 and j<listLen:
        print(list1[j][0:-1])
        j+=1
    return

def artistScrolling(uid,list1, i, conn):
    c = conn.cursor()
    if i < 0:
        i = 0
    if i+5 > len(list1):
        i = len(list1)-5
    showFive(list1, i)
    action = input("Enter:\nw to scroll up\ns to scroll down\n1 to select an artist\nanything else to return to the main menu: ").lower()
    if action=='w':
        if artistScrolling(uid, list1, i-5, conn) == True:
            return True
    elif action=='s':
        if artistScrolling(uid, list1, i+5, conn) == True:
            return True 
    elif action == '1':
        aid = input("Enter the artist's id: ")
        if artistInfo(uid, aid, conn) == True: # return True to return to the main menu
            return True
    else:
        return True

def artistInfo(uid, aid, conn):
    c = conn.cursor()
    getArtistInfo = '''
    SELECT DISTINCT s.sid, s.title, s.duration
    FROM songs s, perform p
    WHERE p.aid = :aid AND p.sid = s.sid;
    '''
    c.execute(getArtistInfo, {'aid':aid})
    songs = c.fetchall()
    if artistSongScrolling(uid, songs, 0, conn) == True:
        return True # True to return to the main menu

def showFiveSongs(list1, i):
    listLen = len(list1)
    if listLen == 0:
        i = 0
    else:
        i = i % listLen
    clear()
    j = i
    print("---Selected Artist's Songs---")
    print("id   |   title   |   duration")
    while j<i+5 and j<listLen:
        print(list1[j][0:-1])
        j+=1
    return

def artistSongScrolling(uid,list1, i, conn):
    c = conn.cursor()
    if i < 0:
        i = 0
    if i+5 > len(list1):
        i = len(list1)-5
    showFiveSongs(list1, i)
    action = input("Enter:\nw to scroll up\ns to scroll down\n1 to select a song\nanything else to return to the main menu: ").lower()
    if action=='w':
        if artistSongScrolling(uid, list1, i-5, conn) == True:
            return True
    elif action=='s':
        if artistSongScrolling(uid, list1, i+5, conn) == True:
            return True 
    elif action == '1':
        sid = input("Enter the song's id: ")
        clear()
        if songActions(uid, sid, conn) == True: # return True to return to the main menu
            return True
    else:
        return True