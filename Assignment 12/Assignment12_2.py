
class Circle: 
    
    PI = 3.14
    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def accept(self):
        self.radius = float(input("Enter the radius of the circle: "))

    
    def calculateArea(self):
        self.area = Circle.PI * self.radius * self.radius

    
    def calculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    
    def display(self):
        print("Radius:", self.radius)
        print("Area:", self.area)
        print("Circumference:", self.circumference)
        

def main():
    
    print("Circle 1:")
    circle1 = Circle()
    circle1.accept()
    circle1.calculateArea()
    circle1.calculateCircumference()
    circle1.display()

    
    print("Circle 2:")
    circle2 = Circle()
    circle2.accept()
    circle2.calculateArea()
    circle2.calculateCircumference()
    circle2.display()

if __name__ == "__main__":
    main()