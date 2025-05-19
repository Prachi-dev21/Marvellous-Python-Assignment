
def CheckNum(N):
    if N % 2 == 0:
        Res = (f"{N} is a Even Number")
    else:
        Res = (f"{N} is an Odd Number")
    return Res

if __name__ == "__main__":
    Ans = int(input("Enter the Number\n"))
    Number = CheckNum(Ans)
    print(Number)