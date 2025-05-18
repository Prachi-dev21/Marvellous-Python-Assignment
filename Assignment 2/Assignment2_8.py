

def Number(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j+1,end = " ")
        print()

if __name__ == "__main__":
    a = int(input("Enter the Number\n"))
    Num = Number(a)