import os
def main():

    print("Enter the file you want to read")
    
    Filename = input()

    ret = os.path.exists(Filename)

    if(ret == True):
        print("File is present in the current directory")
        fobj = open(Filename,"r")
        data = fobj.read()

        print("Data from file is : ",data)

        fobj.close()
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()