def main():
    
    filename = input("Enter the file name: ")
    string = input("Enter the string to search: ")

    fobj = open(filename, 'r')
    data = fobj.read()
    fobj.close()


    count = data.count(string)

    
    print(f"The string '{string}' appears {count} time in the file.")

if __name__ == "__main__":
    main()