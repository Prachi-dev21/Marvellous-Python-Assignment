import multiprocessing

def Fact(N):
    Mul =  1
    for i in range (N, 1, -1):
        Mul = i * Mul
    return Mul

def main():

    numbers = list(map(int, input("Enter the numbers: ").split()))

    pool = multiprocessing.Pool()
    Res = pool.map(Fact, numbers)
    
    print(Res)

if __name__ == "__main__":
    
    main()