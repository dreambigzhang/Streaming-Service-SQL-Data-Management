import sqlite3
from createPlaylist import createPlaylist
import startSession
conn = sqlite3.connect('./a2.db')

c = conn.cursor()
c.execute('PRAGMA foreign_keys=ON;')

def listen(uid, sid):
    # beta test works
    # decide if user has session
    sno = startSession.startSession(uid) # returns the sno of currently active session or newly created session
    # decide if user already listened to the song in the same session
    
    if haveListened(uid, sid, sno):
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
    print(uid, "listened to song", sid, "during session", sno)

def haveListened(uid, sid, sno):
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
def songInfo(sid):
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
#songInfo(10)

def addSongToPlaylist(uid, sid):
    # beta test works
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
        # add later: need to verify that pid is valid and belongs to user
        # add later: need to check if song already in playlist
        getSorder = '''
        SELECT MAX(pl.sorder)+1
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

#addSongToPlaylist('u25', 26)
conn.close()
