#Author: Billy Wood
import login, os
#import addInformation


dirPath = os.getcwd() + "/user"

if(os.path.exists(dirPath) == False):
    os.makedirs(dirPath)
else: pass




def main():
    login.main()
    #addInformation.main()

if __name__ == "__main__":
    main()
