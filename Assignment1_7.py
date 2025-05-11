
def Num(Number):
    if Number % 5 == 0:
        ans = "True"
    else:
        ans = "False"

    return ans

if __name__ == "__main__":

    Val = int(input("Enter the Number\n"))
    res = Num(Val)
    print(res)   


    