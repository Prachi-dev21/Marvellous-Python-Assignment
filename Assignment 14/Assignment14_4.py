class Student:
   
    school_name = "ABC Public School"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"School: {Student.school_name}")


def main():
   
    print("Enter details for first student:")
    name1 = input("Enter Name: ")
    roll1 = int(input("Enter Roll No: "))
    s1 = Student(name1, roll1)

    print("\nEnter details for second student:")
    name2 = input("Enter Name: ")
    roll2 = int(input("Enter Roll No: "))
    s2 = Student(name2, roll2)

    print("\nStudent 1 Details:")
    s1.display()

    print("\nStudent 2 Details:")
    s2.display()

    # Changing class variable using class name
    Student.school_name = input("\nEnter new school name to change for all students: ")

    print("\nAfter changing the school name:")

    print("\nStudent 1 Details:")
    s1.display()

    print("\nStudent 2 Details:")
    s2.display()


if __name__ == "__main__":
    main()