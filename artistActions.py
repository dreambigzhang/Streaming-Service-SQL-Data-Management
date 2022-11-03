
import sqlite3
from scrolling import clear

def artistsMainMenu(aid, conn):

    print("------Artist Main Menu-------")
    action = input("Enter\n1 add a song\n2 find top fans and playlists\n3 to logout\nAnything else to exit the program\n")

    if action == '1':
        clear()
        addSong(aid, conn)
        return artistsMainMenu(aid, conn)
    elif action == '2':
        clear()
        displayUsersPlaylists(aid, conn)
        return artistsMainMenu(aid, conn)
    elif action == '3':
        clear()
        print("logged out")
        return '4' # should return to main screen
    else:
        return -1

def displayUsersPlaylists(aid, conn):

    print("------Top Three Users------")
    users = topThreeUsers(aid, conn)
    if users != None:
        for i in range(len(users)):
            print(" | ".join(users[i]))

    print("\n------Top Three Playlists------")
    playlists = topThreePlaylists(aid, conn)
    if playlists!= None:
        for i in range(len(playlists)):
            print(" | ".join(playlists[i]))

    input("press enter to continue")

def topThreeUsers(aid, conn):

    c = conn.cursor()

    getTopUsers = f"""
    SELECT u.*
    FROM songs s, listen l, perform p, users u
    WHERE s.sid = l.sid AND s.sid = p.sid
    AND p.aid = ?
    AND l.uid = u.uid
    GROUP BY l.uid
    ORDER BY SUM(s.duration * l.cnt) DESC
    LIMIT 3;
    """

    c.execute(getTopUsers, (aid,))
    topUsers = c.fetchall()
    return topUsers

def topThreePlaylists(aid, conn):

    c = conn.cursor()

    getTopPlaylists = f"""
    SELECT p.*
    FROM plinclude pl, perform pr, playlists p
    WHERE pl.sid = pr.sid AND p.pid = pl.pid
    AND pr.aid = ?
    GROUP BY pl.pid
    ORDER BY COUNT(pl.sid) DESC
    LIMIT 3
    """

    c.execute(getTopPlaylists, (aid,))
    topPlaylists = c.fetchall()
    topPlaylists = [list(i) for i in topPlaylists]
    topPlaylists = [[str(i[0])] + i[1:] for i in topPlaylists]
    return topPlaylists


def addSong(aid, conn):

    c = conn.cursor()
    print("------Add a new song------")
    title = input("Enter the title of the song: ")
    if title == "":
        print("ERROR: title cannot be empty")
        input("press enter to continue")
        return
    try:
        duration = int(input("Enter the duration: "))
    except:
        print("ERROR: duration must be an integer")
        input("press enter to continue")
        return


    if not isNewSong(aid, title, duration, conn):
        print("Song with the same title and duration already exists")
        choice = input("Enter\n1 to proceed with adding the song\nAnything else to reject it\n")
        if choice!= '1':
            return
    
    ids = [aid] + input("Enter the aids of any additional artists separated by spaces: ").split()
    if aid in ids[1:]:
        print("ERROR: cannot use own aid as additional aid")
        input("press enter to continue")
        return

    sid = getUniqueSid(conn)

    insertSong = f"""
    INSERT INTO songs 
    VALUES (?, ?, ?);
    """

    c.execute(insertSong, (sid, title, duration))

    if False in [isValidAid(i, conn) for i in ids]:
        print("ERROR: you must enter valid aids")
        addPerformer(ids[0], sid, conn)
        input("press enter to continue")
        return

    for id in ids:
        addPerformer(id, sid, conn)
    conn.commit()
    input("press enter to continue")

def addPerformer(aid, sid, conn):

    c = conn.cursor()
    insertPerform = f"""
    INSERT INTO perform 
    VALUES (?, ?);
    """
    c.execute(insertPerform, (aid, sid))
    conn.commit()

def isValidAid(aid, conn):

    c = conn.cursor()
    getArtist = f"""
    SELECT *
    FROM artists
    WHERE aid = ?;
    """

    c.execute(getArtist, (aid,))
    return bool(c.fetchone())

def getUniqueSid(conn):

    c = conn.cursor()
    sidQuery = """
    SELECT sid
    FROM songs
    """

    c.execute(sidQuery)
    sids = c.fetchall()
    if sids == []:
        return 1
    return max([i[0] for i in sids]) + 1


def isNewSong(aid, title, duration, conn):

    c = conn.cursor()
    songQuery = f"""
    SELECT *
    FROM artists a, songs s, perform p
    WHERE a.aid = p.aid AND s.sid = p.sid
    AND title = ? AND duration = ?
    AND a.aid = ?;
    """

    c.execute(songQuery, (title, duration, aid))
    return not bool(c.fetchone())

if __name__ == "__main__":
    #db = sqlite3.connect("./new.db")
    #topThreePlaylists("a10", sqlite3.connect("./a2.db"))
    #print(isNewSong("a1", "Applause", 212, sqlite3.connect("./a2.db")))
    #print(type(getAllSids(sqlite3.connect("./new.db"))[0]))
    #print(isValidAid("a10", sqlite3.connect("./new.db")))
    #addSong("a10", sqlite3.connect("./new.db"))
    artistsMainMenu("a10", sqlite3.connect("./new.db"))
    #print(getUniqueSid(sqlite3.connect("./new.db")))
    pass