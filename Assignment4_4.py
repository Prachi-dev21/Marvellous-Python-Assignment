

from functools import reduce 

#def CheckEven(No):
    #return (N % 2 == 0)
    
CheckEven = lambda N : (N % 2 == 0)

#def Square(No):
   # return No**2

Square = lambda N : N**2

#def Sum(A,B):
    #return A+B

Sum = lambda A,B : A+B

Data = [5,2,3,4,3,4,1,2,8,10]
print("Input Data : ",Data)

FData = list(filter(CheckEven, Data))
print("Filter Output : ",FData)

MData = list(map(Square, FData))
print("Mapped Output : ",MData)

RData = reduce(Sum, MData)
print("Reduced Output : ",RData)