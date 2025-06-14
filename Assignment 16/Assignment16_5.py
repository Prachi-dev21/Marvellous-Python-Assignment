def main():
    filename = input("Enter the file name: ")

    fobj = open(filename, 'r')

    print("\nLines with more than 5 words:\n")
    for line in fobj:
        words = line.split()
        if len(words) > 5:
            print(line)

    fobj.close()

if __name__ == "__main__":
    main()