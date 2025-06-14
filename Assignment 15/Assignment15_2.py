import os

def main():
    print("Enter the filename you want to create")
    Filename = input()

    fobj = open(Filename, 'w')

    print("Enter the data you want to write in the file")

    data = input()
    fobj.write(data)

    print("Enter the file that you want to read")

    ret = os.path.exists(Filename)

    if (ret == True):

        print("File from directory is present")
        fobj = open(Filename, 'r')
        data = fobj.read()

        print("Data from file is : ", data)
        fobj.close()
    else:
        print("There is no such file")
   

if __name__ == "__main__":
    main()