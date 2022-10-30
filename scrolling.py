# import only system from os

from os import system, name
from playlistInfo import playlistInfo
from songActions import songActions

def clear(): # need to test this works on lab machine
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
 

# now call function we defined above
#clear()

#list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
def showFive(list1, i):
    listLen = len(list1)
    if listLen == 0:
        i = 0
    else:
        i = i % listLen
    
    clear()
    j = i
    print("---Search Result---")
    print("id   |   title   |   duration   |   type")
    while j<i+5 and j<listLen:
        print(list1[j][0:-1])
        j+=1
    return
def scrolling(uid,list1, i, conn):
    c = conn.cursor()
    if i < 0:
        i = 0
    if i+5 > len(list1):
        i = len(list1)-5
    showFive(list1, i)
    action = input("Enter:\nw to scroll up\ns to scroll down\n1 to select a song\n2 to select a playlist\nanything else to return to the main menu: ").lower()
    if action=='w':
        if scrolling(uid, list1, i-5, conn) == True:
            return True
    elif action=='s':
        if scrolling(uid, list1, i+5, conn) == True:
            return True 
    elif action == '1':
        sid = input("Enter the song's id: ")
        if songActions(uid, sid, conn) == True: # return True to return to the main menu
            return True
    elif action == '2':
        pid = input("Enter the playlist's id: ")
        if playlistInfo(uid, pid, conn)==True:
            return True
    else:
        return True

#scrolling(list1, 0) # testing purpose