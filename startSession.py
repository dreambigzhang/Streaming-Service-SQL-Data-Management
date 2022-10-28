
def sessionActive(uid, conn): 
    c = conn.cursor()
    # beta test works
    # false if there's no active session otherwise get sno
    checkSessionActive = '''
    SELECT se.sno
    FROM sessions se
    WHERE se.uid = :uid
    AND se.end IS NULL;'''
    c.execute(checkSessionActive, {'uid':uid});
    activeSession = c.fetchall()
    if activeSession != []:
        sno = activeSession[0][0]
        return sno
    else:
        return False

def startSession(uid, conn): 
    c = conn.cursor()
    # returns the sno of currently active session or newly created session
    # beta test works
    # check if user already has active session
    sno = sessionActive(uid, conn) # false if there's no active session otherwise get sno
    if sno!= False:
        print("*There is already an active session", sno)
        return sno
    else:
        getSno = '''
        SELECT MAX(se.sno)+1
        FROM sessions se
        WHERE se.uid = :uid;
        '''
        c.execute(getSno, {'uid':uid})
        sno = c.fetchone()[0] # let sno be the max(sno) for the user plus 1
        newSession = '''
        INSERT INTO sessions
        VALUES (:uid, :sno, strftime('%Y-%m-%d','now'), NULL);'''
        c.execute(newSession, {'uid':uid, 'sno':sno})
        conn.commit()
        print("*New session created", sno)
        return sno
        




    
#startSession('u1', conn) # testing
