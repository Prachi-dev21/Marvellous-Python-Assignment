
def Number(n):
    for i in range(n):
        for j in range(1,n+1):
            print(j,end = " ")
        print()

if __name__ == "__main__":
    a = int(input("Enter the Number\n"))
    Num = Number(a)
    
#Using while loop

'''
def Star(n):
    
    for i in range(n):
        count = 1
        while(count <= n):
            print(count,end = " ")
            count += 1
        print()

if __name__ == "__main__":
    a = int(input("Enter the Number\n"))
    Num = Star(a)
    
'''
    
