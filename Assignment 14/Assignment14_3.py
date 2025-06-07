class Book:
    def __init__(self, title, price):
        self.title = title
        self.__price = price  
    
    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be greater than 0.")


    def display(self):
        print(f"Title: {self.title}")
        print(f"Price: ₹{self.__price}")


def main():
    title = input("Enter the book title: ")
    price = float(input("Enter the book price: "))

    book1 = Book(title, price)

    print("\nBook Details:")
    book1.display()


    print("\nCurrent Price:", book1.get_price())
    
    new_price = float(input("Enter new price to update: "))
    book1.set_price(new_price)

    print("\nUpdated Book Details:")
    book1.display()


if __name__ == "__main__":
    main()
