
def CheckNum(n):
    if n % 2 != 0:
        Res = "Prime"
    else:
        Res = "Not Prime"
    return Res

if __name__ == "__main__":
    a = int(input("Enter the Number\n"))
    Ans = CheckNum(a)
    print(Ans)
    