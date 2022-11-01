from createPlaylist import createPlaylist
from playlistCheck import songInPlaylist, userOwnsPlaylist
from startSession import startSession
from os import system, name

def clear(): # need to test this works on lab machine
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    
def listen(uid, sid, conn):
    c = conn.cursor()
    clear()
    # beta test works
    # decide if user has session
    sno = startSession(uid, conn) # returns the sno of currently active session or newly created session
    # decide if user already listened to the song in the same session
    
    if haveListened(uid, sid, sno, conn):
        # update table
        updateListen = '''
        UPDATE listen
        SET cnt = cnt+1
        WHERE uid = :uid AND sno = :sno AND sid = :sid;'''
        c.execute(updateListen, {'uid':uid, 'sno':sno, 'sid':sid})
    else: # if have not listened in the current session by current user yet
        insertToListen = '''
        INSERT INTO listen
        VALUES (:uid, :sno, :sid, 1);'''
        c.execute(insertToListen, {'uid':uid, 'sno':sno, 'sid':sid})
    conn.commit()
    clear()
    print("*",uid, "listened to song", sid, "during session", sno)
    input("Enter anything to return to the main menu: ")
    return True
    
    
def haveListened(uid, sid, sno, conn):
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys=ON;')
    haveListened = '''
    SELECT *
    FROM listen l
    WHERE l.uid = :uid AND l.sno = :sno AND l.sid = :sid;
    '''
    c.execute(haveListened, {'uid':uid, 'sno':sno, 'sid':sid})
    listened = c.fetchall()
    if listened != []:
        return True
    else:
        return False
#listen('u5', 6)
'''
More information for a song is the 
names of artists who performed it in addition to 
id, title and duration of the song as well as the 
names of playlists the song is in (if any)'''
def songInfo(sid, conn):
    c = conn.cursor()
    clear()
    # beta test works
    # need to add later: see if sid input is valid sid
    songInfo = '''
    SELECT DISTINCT a.name
    FROM (songs s LEFT OUTER JOIN perform p ON s.sid = p.sid)
    LEFT OUTER JOIN artists a ON p.aid = a.aid
    WHERE s.sid = :sid;'''
    c.execute(songInfo, {'sid':sid})
    artists = c.fetchall()
    print("Artist(s):")
    for artist in artists:
        print(artist[0])
    songInfo = '''
    SELECT DISTINCT s.sid, s.title, s.duration
    FROM songs s
    WHERE s.sid = :sid;'''
    c.execute(songInfo, {'sid':sid})
    songDetail = c.fetchall()
    print("sid:", songDetail[0][0], "\ntitle:", songDetail[0][1], "\nduration(sec):", songDetail[0][2])
    getPlaylists = '''
    SELECT DISTINCT p.title
    FROM ((songs s LEFT OUTER JOIN perform p ON s.sid = p.sid)
    LEFT OUTER JOIN plinclude pl ON s.sid = pl.sid)
    LEFT OUTER JOIN playlists p ON pl.pid = p.pid
    WHERE s.sid = :sid;'''
    c.execute(getPlaylists, {'sid':sid})
    playlists = c.fetchall()
    print("Playlists", songDetail[0][1], "is in:")
    for playlist in playlists:
        print(playlist[0])
    input("Enter anything to return to the main menu: ")
    return True
#songInfo(10)

def addSongToPlaylist(uid, sid, conn):
    c = conn.cursor()    # beta test works
    clear()
    getPlaylists = '''
    SELECT p.pid, p.title
    FROM playlists p
    WHERE p.uid = :uid;
    '''
    c.execute(getPlaylists, {'uid':uid})
    playlists = c.fetchall()
    if playlists==[]:
        print("You have no playlists")
        createPlaylist(uid)
    else:
        print("Here are your playlists")
        for playlist in playlists:
            print(playlist[0], playlist[1])
        pid = input("Enter the pid of playlist you wish to add the song to: ")
        
        if userOwnsPlaylist(uid, pid, conn) == True: #need to verify that pid is valid and belongs to user
        # add later: need to check if song already in playlist
            if songInPlaylist(pid, sid, conn):
                print("This song is already in the selected playlist")
                input("Enter anything to return to the main menu: ")
                return True
            getSorder = '''
            SELECT ifnull(MAX(pl.sorder),0)+1
            FROM plinclude pl
            WHERE pl.pid = :pid;'''
            c.execute(getSorder, {'pid': pid})
            sorder = c.fetchone()[0]
            insertIntoPlaylist = '''
            INSERT INTO plinclude VALUES (:pid, :sid, :sorder);
            '''
            c.execute(insertIntoPlaylist, {'pid': pid, 'sid': sid, 'sorder': sorder})
            conn.commit()
            print("Song", sid, "added to playlist", pid, "at position", sorder)
        else:
            print("*You don't own the playlist entered and cannot add songs to it!")
    input("Enter anything to return to the main menu: ")
    return True

def sidValid(sid,conn):
    c = conn.cursor()
    query = '''
    SELECT *
    FROM songs s
    WHERE s.sid = :sid;'''
    c.execute(query,{'sid':sid})
    result = c.fetchall()
    if result ==[]:
        return False
    else:
        return True

def songActions(uid, sid, conn):
    if not sidValid(sid, conn):
        print(sid,"is not a valid sid")
        input("Enter anything to return to the main menu")
        return True
    else:
        print("Song",sid,"selected")
        action = input("Enter:\n1 to listen\n2 to see more information about it\n3 to add it to a playlist\nanything else to return to the main menu\n")
        if action == '1':
            if listen(uid, sid, conn)== True:
                return True
        elif action == '2':
            if songInfo(sid, conn) == True:
                return True
        elif action == '3':
            if addSongToPlaylist(uid, sid, conn)== True:
                return True
        else:
            return True

