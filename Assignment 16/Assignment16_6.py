import os

def main():
    
    if os.path.exists("source.txt"):
        source = open("source.txt", 'r')
        data = source.read()
        source.close()

        destination = open("destination.txt", 'w')
        destination.write(data)
        destination.close()

        print("Copy successfull from source.txt to destination.txt.")
    else:
        print("source.txt file does not exist.")
if __name__ == "__main__":
    main()