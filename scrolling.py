# import only system from os

from os import system, name

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
    i  = i % listLen
    clear()
    currentlyDisplayedID = []
    j = i
    print("---Search Result---")
    print("id   |   title   |   duration   |   type")
    while j<i+5 and j<listLen:
        currentlyDisplayedID.append(list1[j][0])
        print(list1[j][0:-1])
        j+=1
    return currentlyDisplayedID
def scrolling(uid,list1, i, conn):
    c = conn.cursor()
    if i < 0:
        i = 0
    if i+5 > len(list1):
        i = len(list1)-5
    currentlyDisplayedID = showFive(list1, i)
    action = input("Enter:\nw to scroll up\ns to scroll down\n1 to select a song\n2 to select a playlist\nanything else to return to the main menu: ").lower()
    if action=='w':
        if scrolling(uid, list1, i-5, conn) == True:
            return True
    elif action=='s':
        if scrolling(uid, list1, i+5, conn) == True:
            return True 
    elif action == '1':
        sid = input("Enter the song's id")
        songActions(uid, sid, conn)

#scrolling(list1, 0) # testing purpose