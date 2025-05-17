
def Add(N):
    add = 0
    
    while N > 0:

        Num = N % 10
        add = add + Num
        N = N // 10
        
        
    return add

if __name__ == "__main__":
    a = int(input("Enter the Number\n"))
    Num = Add(a)
    print(Num)