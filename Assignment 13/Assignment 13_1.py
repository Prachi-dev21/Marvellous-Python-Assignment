class Bookstore:
   
    NoOfBooks = 0

    
    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        Bookstore.NoOfBooks += 1

    
    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {Bookstore.NoOfBooks}")


def main():
    obj1 = Bookstore("Linux system programming", "Robert Love")
    obj1.Display()   
    obj2 = Bookstore("C Programming", "Denis Ritche")
    obj2.Display()   


if __name__ == "__main__":
    main()