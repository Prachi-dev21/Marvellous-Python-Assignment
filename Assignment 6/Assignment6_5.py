    
def CheckPrime(N): 
    if N < 2:
        return False
    
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True
 
if __name__ == "__main__":

    a = int(input("Enter the Number\n"))
    if CheckPrime(a):
        print(f"{a} is a prime number")
    else:
        print(f"{a} is not a prime number")
