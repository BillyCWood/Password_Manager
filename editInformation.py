###Author: Billy Wood

from driver import dirPath
import linecache

def changePassword(file, line):
    

    fRead = open(file, "r")
    contents = fRead.readlines()
    fRead.close()
    

    looping = True
    while(looping):
        print("\n" + contents[line] + "\n")
        originalInput = input("Enter the current Password\n> ")
        if (("Password: " + originalInput) in contents[line]):
            while(True):
                userInput = input("\nEnter the new Password\n> ")
                inputCheck = input("\nEnter the new Password one more time\n> ")
                if(userInput == inputCheck and userInput != originalInput):
                    contents[line] = contents[line].replace(("Password: " + originalInput),("Password: " + userInput))
                    looping = False
                    break
                else:
                    print("\nThe Password did not match or you entered the original Password. Please try again")
        else:
            print("\nPassword you entered did not match. Please try again.\n")

    """
    for content in contents:
        print(content)
    """
    fWrite = open(file, "w")

    for content in contents:
        fWrite.write(content)
        fWrite.flush()
    fWrite.close()

def changeUsername(file, line):
    

    fRead = open(file, "r")
    contents = fRead.readlines()
    fRead.close()
    

    looping = True
    while(looping):
        print("\n" + contents[line] + "\n")
        originalInput = input("Enter the current Username\n> ")
        if (("Username: " + originalInput) in contents[line]):
            while(True):
                userInput = input("\nEnter the new Username\n> ")
                inputCheck = input("\nEnter the new Username one more time\n> ")
                if(userInput == inputCheck and userInput != originalInput):
                    contents[line] = contents[line].replace(("Username: " + originalInput),("Username: " + userInput))
                    looping = False
                    break
                else:
                    print("\nThe Usernames did not match or you entered the original Username. Please try again")
        else:
            print("\nUsername you entered did not match. Please try again.\n")
    """
    for content in contents:
        print(content)
    """
    fWrite = open(file, "w")

    for content in contents:
        fWrite.write(content)
        fWrite.flush()
    fWrite.close()

def changeEmail(file, line):
    

    fRead = open(file, "r")
    contents = fRead.readlines()
    fRead.close()
    

    looping = True
    while(looping):
        print("\n" + contents[line] + "\n")
        originalInput = input("Enter the current Email address\n> ")
        if (("Email: " + originalInput) in contents[line]):
            while(True):
                userInput = input("\nEnter the new Email address\n> ")
                inputCheck = input("\nEnter the new Email address one more time\n> ")
                if(userInput == inputCheck and userInput != originalInput):
                    contents[line] = contents[line].replace(("Email: " + originalInput),("Email: " + userInput))
                    looping = False
                    break
                else:
                    print("\nThe Email address did not match or you entered the original email address. Please try again")
        else:
            print("\nEmail address you entered did not match. Please try again.\n")

    for content in contents:
        print(content)

    fWrite = open(file, "w")

    for content in contents:
        fWrite.write(content)
        fWrite.flush()
    fWrite.close()



def main(fileToEdit, lineToEdit):

    file = fileToEdit
    line = lineToEdit
    
    looping = True

    while(looping):

        print("What do you want to edit?\
            \n1. Email\
            \n2. Username\
            \n3. Password\
            \n4. Go Back\
            \n(Type a number)")

        choice = input("> ")
        
        if choice == "1":
            changeEmail(file, line)
        elif choice == "2":
            changeUsername(file, line)
        elif choice == "3":
            changePassword(file, line)
        elif choice == "4":
            looping = False
        else:
            print("\nInvalid Input\n")