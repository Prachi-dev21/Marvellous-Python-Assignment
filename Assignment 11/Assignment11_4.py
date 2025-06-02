
i = 1
Res = 1
def Calculate_Power(x, n):
    global i, Res
    if i <= n:
        Res = Res * x
        i += 1
        Calculate_Power(x, n)
    return Res

def main():
    Num = int(input("Enter the Number: "))
    Power = int(input("Enter the Power to be calculated: "))
    ret = Calculate_Power(Num, Power )
    print(ret)
   

if __name__ == "__main__":
    main()