
def Fact(n):
    f = 1
    for i in range(1,n+1):   #[5,4,3,2,1]
        f = f*i
    return f

if __name__ == "__main__":
    a = int(input("Enter the Number\n"))
    fact = Fact(a)
    print(fact)