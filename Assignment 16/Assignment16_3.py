def main():
  
    filename = input("Enter the file name: ")

    fobj = open(filename, 'r')

    lines = 0
    words = 0
    char = 0

    for line in fobj:
        lines += 1
        words += len(line.split())
        char += len(line)

    fobj.close()

    print(f"Total Lines: {lines}")
    print(f"Total Words: {words}")
    print(f"Total Characters: {char}")

if __name__ == "__main__":
    main()