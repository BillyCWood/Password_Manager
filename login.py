###Author: Billy Wood

import getpass
import os
import sys
import time


dirPath = "C:/Users/billy/CompSci/PythonProg/PasswordProject/users"

dir = os.listdir(dirPath)

def checkPassword(inputFile, userPassword):
    f = open(inputFile)
    if "User Password: " + userPassword in inputFile:
        print("User verified.\n")
        return True
    else:
        return False
    f.close()

def createUser():

    looping = True
    
    print("Creating New User")
    print("-----------------\n\n")
    
    ###loop incase a user is making a duplicate user
    while(looping):
        username = input("Enter username:\n")
        if username+".txt" in dir:
            print("\nThat user already exists.")
            print("-------------------------\n")
        else:
            ###break out of loop
            looping = False

    
    password = getpass.getpass("\nEnter a login password:\n")
    passCheck = getpass.getpass("Please re-enter your password:\n")

    ###loop until password verification passes
    looping = True
    while(looping):
    
        if password != passCheck:
            print("The passwords did not match. Please try again.")
            print("----------------------------------------------\n")
            password = getpass.getpass("Enter a login password:\n")
            passCheck = getpass.getpass("Please re-enter your password:\n")
        else:
            ###break out of loop
            looping = False

    ###write file in the specified directory and use the user's username as the file name
    completePath = (os.path.join(dirPath, username+".txt"))

    f = open(completePath, "w")
    f.write("Username: " + username)
    f.write("\nUser Password: " + password)

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
    for file in dirPath:
        print(file)
    print("Return to Home Screen (Type Return)")

    choice = input("\n")
    while(looping):
        if (choice + ".txt") in dirPath:
            looping = False
        elif (choice.lower() == "return"):
            mainScreen()
        else:
            print("User not found. Please try again.\n")
            choice = input("\n")
        

    password = getpass.getpass("\nEnter password:\n")

    while(verified == False):
        verified = checkPassword(os.path.join(dirPath, (choice + ".txt")), password)

    ###Call next state



def mainScreen():
    looping = True
    choice = input("\n\nWelcome to Password Manager!\n-----------------------------\n\nWhat would you like to do?\n1. Login\n2. Create new User\n3. Exit\n\n")

    while(looping):
        if(choice == "1" or choice.lower() == "login"):
            login()
            looping = False
        elif(choice == "2" or choice.lower() == "create new user"):
            createUser()
            looping = False
        elif(choice == "3" or choice.lower() == "exit"):
            sys.exit()
        else:
            print("Invalid input\n")



def main():
    mainScreen()


main()