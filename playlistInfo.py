import sqlite3
from os import system, name
from songActions import songActions

def clear(): # need to test this works on lab machine
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
 

# now call function we defined above
#clear()

#list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
def showFive(list1, i):
    listLen = len(list1)
    if listLen == 0:
        i = 0
    else:
        i = i % listLen
    
    clear()
    j = i
    print("---Songs in the selected playlist---")
    print("id   |   title   |   duration")
    while j<i+5 and j<listLen:
        print(list1[j][0:-1])
        j+=1
    return

def playlistScrolling(uid,list1, i, conn):
    c = conn.cursor()
    if i < 0:
        i = 0
    if i+5 > len(list1):
        i = len(list1)-5
    showFive(list1, i)
    action = input("Enter:\nw to scroll up\ns to scroll down\n1 to select a song\nanything else to return to the main menu: ").lower()
    if action=='w':
        if playlistScrolling(uid, list1, i-5, conn) == True:
            return True
    elif action=='s':
        if playlistScrolling(uid, list1, i+5, conn) == True:
            return True 
    elif action == '1':
        sid = input("Enter the song's id: ")
        clear()
        if songActions(uid, sid, conn) == True: # return True to return to the main menu
            return True
    else:
        return True

def playlistInfo(uid, pid, conn):
    c = conn.cursor()
    getPlaylistInfo = '''
    SELECT DISTINCT s.sid, s.title, s.duration
    FROM songs s, plinclude pl
    WHERE pl.pid = :pid AND pl.sid = s.sid;
    '''
    c.execute(getPlaylistInfo, {'pid':pid})
    songs = c.fetchall()
    if playlistScrolling(uid, songs, 0, conn) == True:
        return True # True to return to the main menu

#playlistInfo('u1', 2, conn)