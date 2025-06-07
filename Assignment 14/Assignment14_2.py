class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    
    def compute_area(self):
        return self.length * self.width

    
    def compute_perimeter(self):
        return 2 * (self.length + self.width)

    
    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.compute_area()}")
        print(f"Perimeter: {self.compute_perimeter()}")


def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    rect = Rectangle(length, width)
    print("\nRectangle Details:")
    rect.display()


if __name__ == "__main__":
    main()