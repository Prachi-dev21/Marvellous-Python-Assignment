class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)  
        self.subject = subject
        self.salary = salary

    def display(self):
        super().display()  
        print("Subject:", self.subject)
        print("Salary:", self.salary)

def main():
    t1 = Teacher("Niraj", 40, "Science", 30000)
    print("Teacher Details:")
    t1.display()

if __name__ == "__main__":
    main()