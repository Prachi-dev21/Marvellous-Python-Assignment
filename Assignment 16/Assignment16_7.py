def main():

    fobj = open("marks.txt", "w")

    for i in range(5):
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        file.write(name + " " + marks + "\n")

    file.close()

    file = open("marks.txt", "r")

    print("Students who scored more than 75 marks:")

    for line in file:
        name, marks = line.split()
        marks = int(marks)
        if marks > 75:
            print(name)

    file.close()

if __name__ == "__main__":
    main()
