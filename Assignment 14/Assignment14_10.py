class Employee:
    def __init__(self, name, department, salary):
        
        self.name = name

        
        self._department = department

        
        self.__salary = salary

   
    def displayInfo(self):
        print("Name:", self.name)
        print("Department :", self._department)
        print("Salary:", self.__salary)

   
    def getSalary(self):
        return self.__salary

 
    def setSalary(self, new_salary):
        self.__salary = new_salary

def main():
    emp = Employee("Pavan", "Engineering", 8000)

  
    print("Name:", emp.name) 

    
    print("Department:", emp._department) 

    
    print("Salary:", emp.getSalary())  

    print("\nTrying to access Private Member directly:")
    try:
        print(emp.__salary)  
    except AttributeError:
        print("Cannot access private variable directly.")

    emp.setSalary(10000)
    print("Updated Salary:", emp.getSalary())

    emp.displayInfo()


if __name__ == "__main__":
    main()
