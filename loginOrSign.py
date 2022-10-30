def loginOrSign(): 
    # get user input on whether to login or sign up
    mainMenuAction = input("Enter\n1 to login\n2 to sign up \nAnything else to exit program\n")
    mainMenuAction = mainMenuAction.strip()  # remove any unneccessary spaces

    print(mainMenuAction)
    return mainMenuAction  # returns 1 for login, 2 for sign up, all else for exit
