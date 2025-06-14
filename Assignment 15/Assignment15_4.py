def main():
   
    file1 = input("Enter the first file name: ")
    file2 = input("Enter the second file name: ")

   
    f1 = open(file1, 'r')
    data1 = f1.read()
    f1.close()

    f2 = open(file2, 'r')
    data2 = f2.read()
    f2.close()


    if data1 == data2:
        print("Files have the same contents.")
    else:
        print("Files have different contents.")

if __name__ == "__main__":
    main()
