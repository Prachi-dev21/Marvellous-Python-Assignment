def main(N):
    data = []
    for i in range(N):
        Num = int(input("Enter the numbers\n"))
        data.append(Num)
    Even = list(filter(lambda N : N % 2 == 0, data))
    return Even


if __name__ == "__main__":
    a = int(input("Enter the size\n"))
    Res = main(a)
    print("Even Numbers : ",Res)
