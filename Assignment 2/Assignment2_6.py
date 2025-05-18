
def Star(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end = " ")
        print()

if __name__ == "__main__":
    a = int(input("Enter the Number\n"))
    Num = Star(a)
    
#Using while loop

'''
def Star(a):

    for i in range(a):
        count = 0
        while (count<(a-i)):
            print("*",end = " ")
            count+=1
        print()

if __name__ == "__main__":
    a = int(input("Enter the Number\n"))
    Num = Star(a)
    
'''

