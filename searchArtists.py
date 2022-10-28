from scrolling import scrolling
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

def dictToList(dict):
    returnList = []
    for pair in dict:
        returnList.append([pair]+dict[pair])
    return returnList

def searchArtists(uid, conn):

    c = conn.cursor()
    print("-----Search for artists-----")
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
    get all matching artists and their songs
    '''
    getArtistAndSongs = '''
    SELECT DISTINCT a.aid, a.name, a.nationality, s.title, s.sid
    FROM artists a, perform p, songs s
    WHERE p.aid = a.aid AND p.sid = s.sid AND (\n'''
    for i in range(len(keywords)):
        if i!=0:
            getArtistAndSongs += "\n OR"
        getArtistAndSongs += " lower(a.name) LIKE '%"+keywords[i].lower()+"%'"
        getArtistAndSongs += " OR lower(s.title) LIKE '%"+keywords[i].lower()+"%'"
    getArtistAndSongs+=');'

   
    #print(getArtistAndSongs)
    c.execute(getArtistAndSongs)
    artistsAndSongs = c.fetchall()
    
    artistsAndSongs = tupleToList(artistsAndSongs)
    #print(artistsAndSongs)
    # use a dictionary structure where aid is the key
    artistDict = {}
    for row in artistsAndSongs:
        if not (row[0] in artistDict):
            artistDict[row[0]]=[row[1],row[2],0,0]
    # add number of songs of a artist
    getNumOfSongs = '''
    SELECT DISTINCT a.aid, COUNT(DISTINCT p.sid)
    FROM artists a, perform p
    WHERE a.aid = p.aid
    GROUP BY a.aid'''
    c.execute(getNumOfSongs)
    NumOfSongs = c.fetchall()
    #print(NumOfSongs)
    for row in NumOfSongs:
        aid = row[0]
        songCount = row[1]
        if aid in artistDict:
            artistDict[aid][2] = songCount
    # count the number of matches for each artist in their song title
    
    for row in artistsAndSongs:
        aid = row[0]
        songTitle = row[3]
        artistDict[aid][-1]+= numOfMatch(songTitle, keywords)
    
    # count the number of matches for each artist in their name
    for aid in artistDict:
        getName = '''
        SELECT DISTINCT a.name
        FROM artists a
        WHERE a.aid = :aid'''
        c.execute(getName, {'aid':aid})
        aName = c.fetchone()[0]
        artistDict[aid][-1]+= numOfMatch(aName, keywords)
    #print(artistDict)
    artistList = dictToList(artistDict)
    #print(artistList)
    if scrolling(uid, artistList, 0, conn)==True:
        return True
    
#list1 = ["The"]
#searchArtists("u1")


