import login
import os
import sys
import driver

dirPath = driver.dirPath

userfile = ""
userName = ""

def chooseOptions():
    print()
    print("\nWhat would you like to do:\
        \n\t1. Add Password (Type Add)\
        \n\t2. Remove Password (Type Remove)\
        \n\t3. Display All Stored Usernames and Passwords (Type Display)\
        \n\t4. Redisplay All available Options (Type Redisplay)\
        \n\t5. Switch Users (Type Logout)\
        \n\t6. Exit (Type Exit)")
def getContents():
    f = open(userfile, "r")
    line =f.readline()
    line = f.readline()
    while True:
        line = f.readline()
        if not line:
            break
        else:
            print(line,end="")
    f.close()

def addToFile():
    f = open(userfile, "a")
    website = input("Enter the website/application name: ")
    email = input ("Enter associated email (Type 'None' if there is no username): ")
    addUserName = input("Enter the associated username (Type 'None' if there is no username): ")
    addPassword = input("Enter the associated password: ")
    writeString = "Website: {0}\tEmail: {1}\tUsername: {2}\tPassword: {3}\n".format(website,email,addUserName,addPassword)

    f.write(writeString)

    f.close()

    sortFile()

def removeFromFile():
    f = open(userfile, "w")
    getContents()
    print("\nWhich account would you like to remove?\n")
    choice = input("> ")
    f.close()

def sortFile():
    f = open(userfile, "r")
    f.close()

def main():
    looping = True

    print("\t\t\t----------", end = "")
    for i in range(0,userName.__len__()+1):
        print("-", end = "")
    print("\n\t\t\t|Welcome, {}|".format(userName))
    print("\t\t\t----------", end = "")
    for i in range(0,userName.__len__()+1):
        print("-", end = "")

    chooseOptions()

    while(looping):
        print()
        choice = input(">")
        print()

        if choice.lower() == "add":
            addToFile()

        elif choice.lower() == "remove":
            pass

        elif choice.lower() == "display":
            print()
            getContents()
            print()

        elif choice.lower() == "redisplay":
            chooseOptions()

        elif choice.lower() == "logout":
            login.mainScreen()

        elif choice.lower() == "exit":
            sys.exit()            

        else:
            print("Invalid Input. Please try again.\n")


    