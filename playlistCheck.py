# check if song already in the playlist
def songInPlaylist(pid, sid, conn):
    c = conn.cursor()
    songInPlaylist = '''
    SELECT *
    FROM plinclude pl
    WHERE pl.pid = :pid AND pl.sid = :sid;'''
    c.execute(songInPlaylist,{'pid':pid, 'sid':sid})
    result = c.fetchall()
    if result == []:
        return False
    else:
        return True
# check if the user owns the playlist
def userOwnsPlaylist(uid, pid, conn):
    c = conn.cursor()
    userOwnsPlaylist = '''
    SELECT *
    FROM playlists p
    WHERE p.uid = :uid AND p.pid = :pid;'''
    c.execute(userOwnsPlaylist,{'uid':uid, 'pid':pid})
    result = c.fetchall()
    if result == []:
        return False
    else:
        return True