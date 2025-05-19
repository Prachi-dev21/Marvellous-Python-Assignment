
def Triangle(N):
    for i in range(N+1):
        for j in range(i):
            print("*", end = " ")
        print()

if __name__ == "__main__":
    
    A = int(input("Enter the Number\n"))
    Triangle(A)