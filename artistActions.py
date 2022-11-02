
import sqlite3
import random
from scrolling import clear

def artistsMainMenu(aid, conn):

    print("------Artist Main Menu-------")
    action = input("Enter\n1 add a song\n2 find top fans\n3 find top playlists\n4 to logout\nAnything else to exit the program\n")

    if action == '1':
        clear()
        addSong(aid, conn)
        artistsMainMenu(aid, conn)
    elif action == '2':
        clear()
        displayUsers(aid, conn)
        artistsMainMenu(aid, conn)
    elif action == '3':
        clear()
        displayPlaylists(aid, conn)
        artistsMainMenu(aid, conn)
    elif action =='4':
        clear()
        print("logged out")
        return '4' # should return to main screen
    else:
        return -1

def displayUsers(aid, conn):

    print("------Top Three Users------")
    users = topThreeUsers(aid, conn)

    for i in range(len(users)):
        print(str(i + 1) + ". " + users[i][0])

    input("press enter to continue")

def displayPlaylists(aid, conn):

    print("------Top Three Users------")
    playlists = topThreePlaylists(aid, conn)

    for i in range(len(playlists)):
        print(str(i + 1) + ". " + playlists[i][0])

    input("press enter to continue")

def topThreeUsers(aid, conn):

    c = conn.cursor()

    getTopUsers = f"""
    SELECT l.uid
    FROM songs s, listen l, artists a, perform p
    WHERE s.sid = l.sid AND s.sid = p.sid
    AND a.aid = p.aid AND a.aid = "{aid}"
    GROUP BY l.uid
    ORDER BY SUM(s.duration * l.cnt) DESC
    LIMIT 3;
    """

    c.execute(getTopUsers)
    topThree = c.fetchall()
    for user in topThree:
        print(user)

def topThreePlaylists(aid, conn):

    c = conn.cursor()

    getTopPlaylists = f"""
    SELECT pl.pid
    FROM plinclude pl, perform pr
    WHERE pl.sid = pr.sid
    AND pr.aid = "{aid}"
    GROUP BY pl.pid
    ORDER BY COUNT(pl.sid) DESC
    LIMIT 3;
    """

    c.execute(getTopPlaylists)
    topPlaylists = c.fetchall()
    for i in topPlaylists:
        print(i)


def addSong(aid, conn):

    c = conn.cursor()
    print("------Add a new song------")
    title = input("Enter the title of the song: ")
    duration = int(input("Enter the duration: "))

    if not isNewSong(aid, title, duration, conn):
        print("ERROR: Song already exists")
        return
    
    ids = [aid] + input("Enter the aids of any additional artists separated by spaces: ").split()
    sid = getUniqueSid(conn)

    insertSong = f"""
    INSERT INTO songs 
    VALUES ({sid}, "{title}", {duration});
    """

    c.execute(insertSong)

    for id in ids:
        insertPerform = f"""
        INSERT INTO perform 
        VALUES ("{id}", {sid});
        """
        c.execute(insertPerform)
    conn.commit()
    input("press enter to continue")

def getUniqueSid(conn):

    allSids = getAllSids(conn)
    sid = allSids[0]

    while sid in allSids:
        sid = random.randint(1, 2 * len(allSids))
    
    return sid

def getAllSids(conn):

    c = conn.cursor()
    sidQuery = """
    SELECT sid
    FROM songs
    """

    c.execute(sidQuery)
    return [i[0] for i in c.fetchall()]


def isNewSong(aid, title, duration, conn):

    c = conn.cursor()
    songQuery = f"""
    SELECT *
    FROM artists a, songs s, perform p
    WHERE a.aid = p.aid AND s.sid = p.sid
    AND title = "{title}" AND duration = {duration}
    AND a.aid = "{aid}";
    """

    c.execute(songQuery)
    return not bool(c.fetchone())

if __name__ == "__main__":
    #topThreePlaylists("a10", sqlite3.connect("./a2.db"))
    #print(isNewSong("a1", "Applause", 212, sqlite3.connect("./a2.db")))
    print(type(getAllSids(sqlite3.connect("./new.db"))[0]))