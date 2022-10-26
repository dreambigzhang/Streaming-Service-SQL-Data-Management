import sqlite3
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

conn.close()
