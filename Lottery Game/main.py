def homePage():
    """This function refer home page"""
    print("WELCOME TO OUR LOTTERY GAME")
    print("\n1:Read Rules\n2:Sign Up\n3:Sign In\n4:Quit\n")#Options for homepage
    userInput = input()
    if userInput == "1" or userInput == "2" or userInput == "3" or userInput == "4":
        if int(userInput) == 1:
            rule()
        elif int(userInput) == 2:
            signUp()
        elif int(userInput) == 3:
            signIn()
        elif int(userInput) == 4:
            quit()
    else:
        print("\nUnknown Input")
        homePage()

def secondPage():
    "This function will display second page"
    userInput = input("\n1:Info\n2:Input\n3:Withdraw\n4:Play Game\n5:Home\n")
    if userInput == "1" or userInput == "2" or userInput == "3" or userInput == "4" or userInput == "5":
        if int(userInput) == 1:
            info(user_count)
        elif int(userInput) == 2:
            amountInput()
        elif int(userInput) == 3:
            withdraw()
        elif int(userInput) == 4:
            playGame()
        elif int(userInput) == 5:
            homePage()
    else:
        print("\nUnknown Input")
        secondPage()

def rule():
    """This function display rules of the game"""
    print("\nPlayer Must Be Over 18")
    print("Player Must Have At Least 5000 MMK")
    print("You Have To Use At least 1000 MMK For Each Guessing")
    print("If You Win, You Will Get 80x Amount")
    homePage()

def signUp():
    """This function for signing up processes"""
    userAge=int(input("\nEnter Your Age:"))#checking age of user
    if not userAge>=18:
        print("Pls Read The Rules Again")
        homePage()
    while True:#requesting username
        userName = input("Enter Username:")
        if userName in name_list:#checking username in name_list
            print("\nUsername Has Been Taken\nPls Use Difference Username")
            userInput =int(input("\n1:Continue\n2:Home\n"))
            if userInput==1:
                continue
            elif userInput==2:
                homePage()
        else:#storig username to name_list
            name_list.append(userName)
            while True:# requesting password
                userPass = input("Enter Password:")
                userPass2 = input("Enter Password To Comfirm:")
                if userPass != userPass2:#checking 2 password same or not
                    print("\nPassword Are Not Same")
                    userInput = int(input("\n1:Re Enter Password\n2:Home\n"))
                    if userInput == 1:
                        continue
                    elif userInput == 2:
                        name_list.pop()
                        homePage()
                else:#storig password to pass_list
                    pass_list.append(userPass)
                    while True:#requesting amount
                        userMoney = int(input("Enter Amount:"))
                        if userMoney<5000:#check the amount >= 5000 MMK
                            print("Sorry!!\nPlayer Must Input At Least 5000 MMK")
                            userInput = int(input("\n1:Re Enter Amount\n2:Home\n"))
                            if userInput == 1:
                                continue
                            elif userInput == 2:
                                name_list.pop()
                                pass_list.pop()
                                homePage()
                        else:#stroing amount to amount_list
                            amount_list.append(userMoney)
                            user_count=name_list.index(userName)#will return index num of user data to user_count
                            secondPage()

def signIn():
    "This function is signing in processes"
    while True:
        userName = input("\nEnter Username To Sign In: ")
        if not userName in name_list:
            print("There Is No User With Username ", userName)
            userInput = int(input("\n1:Re Enter Username\n2:Home\n"))
            if userInput == 1:
                continue
            elif userInput == 2:
                homePage()
        else:
            user_count = name_list.index(userName)
            while True:
                userPass = input("Enter Password To Sign In: ")
                if userPass!=pass_list[user_count]:
                    print("Incorrect Password!!")
                    userInput = int(input("\n1:Re Enter Password\n2:Home\n"))
                    if userInput == 1:
                        continue
                    elif userInput == 2:
                        homePage()
                else:
                    print("Successfully Signed In!!")
                    secondPage()




def playGame():
    """This function is playing processes"""
    print("\nYou Can Start Guessing")
    randomNumber=randNum()#generating random number
    while True:#user is guessing lottery number
        userGuessNum = int(input("Guess Lottery Number:"))
        if userGuessNum<1 or userGuessNum>99:
            print("\nLottery Number Cannot Be Greather Than 99 Or Less Than 1")
            userInput=int(input("\n1:Continue Guessing\n2:Menu\n"))
            if userInput==1:
                continue
            elif userInput==2:
                secondPage()
        else:#user is paying amount
            while True:
                    money = int(input("Enter Money Amount:"))
                    if amount_list[user_count] - money < 0:#amount checking process that user has enough amount or not
                        print("\nNot Enough Money!!")
                        print("You Need To Input Enough Money First")
                        secondPage()
                    elif money<1000:
                         print("You Have To Use At least 1000 MMK For Each Guessing")
                         print("If You Win, You Will Get 80x Amount")
                         userInput=int(input("\n1:Re Enter Money Amount\n2:Menu\n"))
                         if userInput==1:
                            continue
                         elif userInput==2:
                             secondPage()
                    else:
                        print("\nThe Lottery Number is ",randomNumber)
                        if randomNumber!=userGuessNum:#giving or taking money after a round finished
                            amount_list[user_count]=amount_list[user_count]-money
                            print("Sorry!!\nYour Amount: ",amount_list[user_count]," MMK")

                            userInput=int(input("\n1:Try Again\n2:Menu\n"))
                            if userInput == 1:
                                playGame()
                            elif userInput == 2:
                                secondPage()
                        else:
                            amount_list[user_count]=(amount_list[user_count]+(money*80))-money
                            print("Congratulation!!\nYour Amount: ",amount_list[user_count]," MMK")
                            userInput = int(input("\n1:Try Again\n2:Menu\n"))
                            if userInput==1:
                                playGame()
                            elif userInput==2:
                                secondPage()

def info(count):
    "This function will display user info"
    print("\nName:",name_list[count])
    print("Password:",pass_list[count])
    print("Amount:",amount_list[count]," MMK")
    secondPage()

def randNum()->"will return random number":
    """This function is to generate random number"""
    import secrets
    secureGenerator = secrets.SystemRandom()
    randomNumber = secureGenerator.randint(1, 99)
    return randomNumber

def amountInput():
    """This function works amount input processes"""
    amount = int(input("Enter Amount To Input:"))
    amount_list[user_count]=amount_list[user_count]+amount
    print("\nProcess Success!!")
    info(user_count)
    secondPage()

def withdraw():
    """This function works withdraw processes"""
    amount = int(input("Enter Amount To Withdraw:"))
    if amount>amount_list[user_count]:
        print("\nSorry, You Don't Have Enought Amount To Withdraw ",amount," MMK")
        secondPage()
    else:
        amount_list[user_count]=amount_list[user_count]-amount
        print("\nProcess Success!!")
        info(user_count)
        secondPage()

#Working Space
name_list=[]#list for store username data
pass_list=[]#list for store password data
amount_list=[]#list for store amount data
user_count=0#To know index num of user data
homePage()#Program start point