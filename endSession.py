from startSession import sessionActive

def endSession(uid, conn): 
    c = conn.cursor()
    # returns the sno of currently active session or newly created session
    # beta test works
    # check if user already has active session
    sno = sessionActive(uid, conn) # false if there's no active session otherwise get sno
    if sno== False:
        print("You have no active session")
        return None
    else:
        endSession = '''
        UPDATE sessions
        SET end = strftime('%Y-%m-%d','now')
        WHERE uid = :uid AND sno = :sno;'''
        c.execute(endSession, {'uid':uid, 'sno':sno})
        conn.commit()
        print("*"+uid+"'s","session", sno, "ended")
        return sno
#endSession('u1', conn)
