import sys

def main():
    if len(sys.argv) != 2:
        print("")
        return

    FileName = sys.argv[1]
    destination_file = "File.txt"

    
    FName = open(FileName, 'r')
    data = FName.read()
    FName.close()

    
    File = open(destination_file, 'w')
    File.write(data)
    File.close()

    print("File copied to File.txt successfully.")

if __name__ == "__main__":
    main()