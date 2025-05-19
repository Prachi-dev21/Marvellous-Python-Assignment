
def CheckPrime(N):
    
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

def main():
    
    data = list(map(int,input().split()))
    print("****Data", data)
        #Num = int(input("Enter the numbers\n"))
    Prime = list(filter(CheckPrime, data))
    return Prime


if __name__ == "__main__":
    
    Res = main()
    print(Res)
