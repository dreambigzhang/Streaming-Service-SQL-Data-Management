def numOfMatch(str, keywords):
    matchCount = 0
    for keyword in keywords:
        if keyword.lower() in str.lower():
            matchCount+=1
    return matchCount

def tupleToList(listOfTuples): # copy a list of tuple to a list of lists
    returnList = []
    for tuple in listOfTuples:
        sublist = []
        for element in tuple:
            sublist.append(element)
        returnList.append(sublist)
    return returnList

def searchSongsAndPlaylists(uid, conn):
    c = conn.cursor()

    print("Search for songs and playlists")
    keywords = []
    numOfKeywords = int(input("How many keywords: "))
    print("Input the keywords (press enter after every keyword)")
    for i in range(numOfKeywords):
        keyword = input()
        keywords.append(keyword)
    '''
    keywords is a list of keywords
    '''
    '''
    search for songs
    '''
    getSongs = '''
    SELECT DISTINCT s.sid, s.title, s.duration, 'song' as category
    FROM songs s
    WHERE'''
    for i in range(len(keywords)):
        if i!=0:
            getSongs += "\n OR"
        getSongs += " lower(s.title) LIKE '%"+keywords[i].lower()+"%'"
    getSongs+=';'

    #print(getSongs)
    c.execute(getSongs)
    songs = c.fetchall()
    songs = tupleToList(songs)

    '''
    search for playlists
    '''
    getPlaylists = '''
    SELECT DISTINCT p.pid, p.title, SUM(s.duration), 'playlist' as category
    FROM songs s, playlists p, plinclude pl
    WHERE pl.sid = s.sid AND p.pid = pl.pid
    AND ('''
    for i in range(len(keywords)):
        if i!=0:
            getPlaylists += "\n OR"
        getPlaylists += " lower(p.title) LIKE '%"+keywords[i].lower()+"%'"
    getPlaylists+=")\nGROUP BY p.pid, p.title;"
    #print(getPlaylists)
    c.execute(getPlaylists)
    playlists = c.fetchall()
    playlists = tupleToList(playlists)

    # combine song and playlist lists
    songsAndPlaylist = songs + playlists
    #print(songsAndPlaylist)
    # add the numOfMatch to the end of each sublist
    for i in range(len(songsAndPlaylist)):
        songsAndPlaylist[i].append(numOfMatch(songsAndPlaylist[i][1], keywords)) 
        # sort based on the number of keyword matches
    songsAndPlaylist.sort(key=lambda x: x[-1], reverse=True)
    print(songsAndPlaylist)
    

#list1 = ["Kill", "You", "What", "Young", "Music"]
#searchSongsAndPlaylists(list1)


