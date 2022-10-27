# import only system from os
from os import system, name

def clear(): # need to test this works on lab machine
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
 

# now call function we defined above
#clear()

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
def showFive(list1, i):
    listLen = len(list1)
    i  = i % listLen
    clear()
    j = i
    
    while j<i+5 and j<listLen:
        print(list1[j])
        j+=1

def scrolling(list1, i):
    if i < 0:
        i = 0
    if i+5 > len(list1):
        i = len(list1)-5
    showFive(list1, i)
    scroll = input("w to scroll up, s to scroll down. Input anything else to stop viewing: ")
    if scroll.lower()=='w' or scroll.lower()=='s':
        if scroll.lower() == 'w':
            scrolling(list1, i-5)
        elif scroll.lower() == 's':
            scrolling(list1, i+5)
    else:
        print("Viewing ended")

    

scrolling(list1, 0) # testing purpose