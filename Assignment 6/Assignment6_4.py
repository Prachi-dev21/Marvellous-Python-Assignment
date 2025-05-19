
def Fact(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result

if __name__ == "__main__":

    a = int(input("Enter the Number\n"))
    res = Fact(a)
    print(res)
        