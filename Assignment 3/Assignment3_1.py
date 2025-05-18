
from functools import reduce

N = int(input("Enter the number of elements you want to enter in list\n"))

list = []
total = 0
for i in range(N):
    
    Num = int(input("Enter the Numbers\n"))
    list.append(Num)
    total += Num

if __name__=="__main__":

    print(total) 

#Using Reduce  

'''
N = int(input("Enter the number of elements you want to enter in list\n"))

list = []
for i in range(N):
    
    Num = int(input("Enter the Numbers\n"))
    list.append(Num)
    
def Sum(A,B):
    return A+B
if __name__=="__main__":

    Result = reduce(Sum, list)
    print(Result)
'''