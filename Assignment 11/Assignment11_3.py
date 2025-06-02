

i = 0
Sum = 0
def SumofDigits(Num):
    global Sum, i
    Num = str(Num)
    if i < len(Num):
        Sum = Sum + int(Num[i])
        i += 1
        SumofDigits(Num)
    return Sum

def main():
    N = int(input("Enter the Number: "))
    ret = SumofDigits(N)
    print(ret)
   

if __name__ == "__main__":
    main()


    