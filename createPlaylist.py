def createPlaylist(uid, conn):
    c = conn.cursor()
    # beta test works
    title = input("Enter title to create new playlist: ")
    # let pid be max pid +1
    getPid = '''
    SELECT MAX(p.pid)+1
    FROM playlists p'''
    c.execute(getPid)
    pid = c.fetchone()[0]
    insertPlaylist = '''INSERT INTO playlists VALUES (:pid,:title,:uid);'''
    c.execute(insertPlaylist, {'pid':pid, 'title':title, 'uid': uid})
    conn.commit()
    print("New playlist", pid, title, "created by", uid)


#createPlaylist('u1')