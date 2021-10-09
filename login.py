###Author: Billy Wood

import getpass
import os
import sys
import time
import addInformation
import driver


driver.dirPath### = "C:/Users/billy/CompSci/PythonProg/PasswordProject/users"

dir = os.listdir(driver.dirPath)

def checkPassword(inputFile, userPassword):
    f = open(inputFile)
    #get second line
    line = f.readline()
    line = f.readline()
    f.close()
    #print(line[15:])
    if (str(userPassword)+"\n") == line[15:]:
        print("User verified.\n")
        return True
    else:
        print("The password is incorrect. Please try again.\n")
        return False
    

def createUser():

    looping = True
    
    print("Creating New User")
    print("-----------------\n\n")

    
    #loop incase a user is making a duplicate user
    while(looping):
        username = input("Enter username:\n> ")
        if username+".txt" in dir:
            print("\nThat user already exists.")
            print("-------------------------\n")
        else:
            #break out of loop
            looping = False


    #getpass.getpass() hides the inputted string from displaying in cmd
    password = getpass.getpass("\nEnter a login password:\n")
    passCheck = getpass.getpass("Please re-enter your password:\n")


    #loop until password verification passes
    looping = True
    while(looping):
    
        if password != passCheck:
            print("The passwords did not match. Please try again.")
            print("----------------------------------------------\n")
            password = getpass.getpass("Enter a login password:\n")
            passCheck = getpass.getpass("Please re-enter your password:\n")
        else:
            #break out of loop
            looping = False

    #write file in the specified directory and use the user's username as the file name
    completePath = (os.path.join(driver.dirPath, username+".txt"))


    f = open(completePath, "w")
    f.write("Username: " + username)
    f.write("\nUser Password: " + password)
    f.close


    print("User created!\n\nReturning to home screen in:")
    for i in range(-3,0):
        print(abs(i))
        time.sleep(1)
    mainScreen()


def login():
    looping = True
    verified = False

    if len(dir) == 0:
        print("\nThere are currently no users associated with this system.\n")
        createUser()

    print("Which user would you like to login as:\n")
    for file in os.scandir(driver.dirPath + "/"):
        print(file.name[0:-4])
    print("\nReturn to Home Screen (Type Return)")

    user = ""
    while(looping):
        choice = input("\n> ")
        if os.path.exists(driver.dirPath + "/" + choice + ".txt"):
            user = choice
            looping = False
        elif (choice.lower() == "return"):
            mainScreen()
        else:
            print("User not found. Please try again.\n")

    
    #pass the requested file location and user name to the addInformation module
    addInformation.userfile = driver.dirPath + "/" + user + ".txt"
    addInformation.userName = user
            

    while(verified != True):
        password = getpass.getpass("\nEnter password:\n")
        verified = checkPassword(os.path.join(driver.dirPath, (user + ".txt")), password)




def mainScreen():
    looping = True
    choice = input("\nWhat would you like to do?\
        \n\t1. Login\
        \n\t2. Create new User\
        \n\t3. Exit\n\n> ")

    while(looping):
        if(choice == "1" or choice.lower() == "login"):
            looping = False
            login()
        elif(choice == "2" or choice.lower() == "create new user"):
            looping = False
            createUser()
        elif(choice == "3" or choice.lower() == "exit"):
            sys.exit()
        else:
            print("Invalid input\n")



def main():
    print("\n\t\t\t------------------------------\
        \n\t\t\t|Welcome to Password Manager!|\
        \n\t\t\t------------------------------\n")
    mainScreen()
    

if __name__ == "__main__":
    main()

