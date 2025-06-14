import os

def main():

    print("Enter the file you want to check : ")
    Filename = input()

    ret = os.path.exists(Filename)

    if (ret == True):

        print("File is in the directory")
    else:
        print("File dosent exist")

if __name__ == "__main__":
    main()