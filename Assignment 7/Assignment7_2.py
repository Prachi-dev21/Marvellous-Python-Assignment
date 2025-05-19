def main(N):
    data = []
    for i in range(N):
        Num = int(input("Enter the numbers\n"))
        data.append(Num)
    Double = list(map(lambda N : N*2, data))
    return Double


if __name__ == "__main__":
    a = int(input("Enter the size\n"))
    Res = main(a)
    print(Res)
