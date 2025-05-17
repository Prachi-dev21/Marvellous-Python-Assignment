
def count(N):
    c = 0
    for count in str(N):
        c += 1
    return c

if __name__ == "__main__":
    a = int(input("Enter the Number\n"))
    Num = count(a)
    print(Num)

# Using While loop
'''
def count(N):
    c= 0
    if N == 0:
        return 1
    while N > 0:

        N = N // 10
        c += 1
    return c

if __name__ == "__main__":
    a = int(input("Enter the Number\n"))
    Num = count(a)
    print(Num)
'''
  
    
