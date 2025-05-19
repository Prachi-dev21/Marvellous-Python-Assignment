from functools import reduce

def main(N):
    data = []
    for i in range(N):
        Num = int(input("Enter the numbers\n"))
        data.append(Num)
    Product = reduce(lambda A,B: A*B, data)
    return Product


if __name__ == "__main__":
    a = int(input("Enter the size\n"))
    Res = main(a)
    print(Res)
