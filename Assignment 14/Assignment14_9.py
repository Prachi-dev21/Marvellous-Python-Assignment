class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Overriding __eq__ to compare prices only
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False



def main():
    product1 = Product("Watch", 40000)
    product2 = Product("Washing Machine", 30000)
    product3 = Product("Tablet", 40000)

    print("Comparing product1 and product2:")
    if product1 == product2:
        print("Both products have the same price.")
    else:
        print("Products have different prices.")

    print("Comparing product1 and product3:")
    if product1 == product3:
        print("Both products have the same price.")
    else:
        print("Products have different prices.")


if __name__ == "__main__":
    main()