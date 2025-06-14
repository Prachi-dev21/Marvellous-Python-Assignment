def main():

    print("Enter the filename you want to create ")
    Filename = input()

    fobj = open(Filename, 'w')

    print("Enter the name of a students : ")
    data = input()
    fobj.write(data)

    fobj.close()
    print("File  created successfully.")

if __name__ == "__main__":
    main()
    