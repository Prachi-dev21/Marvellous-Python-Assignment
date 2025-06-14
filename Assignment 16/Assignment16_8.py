def main():
    fobj = open("input.txt", "r")

destination = open("output.txt", "w")


for line in fobj:
    if line.strip() != "": 
        destination.write(line)

fobj.close()
destination.close()

print("output.txt")

if __name__ == "__main__":
    main()
