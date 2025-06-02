

fact = 1 
def Factorial(N):
    global fact
    if (N >= 1):
        fact = fact * N
        N = N - 1
        Factorial(N)
    return fact
    
def main():
    Num = int(input("Enter the Number: "))
    ret = Factorial(Num)
    print(ret)
   

if __name__ == "__main__":
    main()