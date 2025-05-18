
def CheckPrime(N):
    if N <= 1:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

if __name__ == "__main__":

    ans = int(input("Enter the number\n"))
    Num = CheckPrime(ans)
    print(Num)