
from functools import reduce 

#def CheckNum(No):
    #return (No>=70 and No <= 90)
    
CheckNum = lambda N : (N >= 70 and N <= 90)

#def Increase(No):
   # return No+10

Increase = lambda N : N+10

#def Product(A,B):
    #return A*B

Product = lambda A,B : A*B

Data = [4,34,36,76,68,24,89,23,86,90,45,70]
print("Input Data : ",Data)

FData = list(filter(CheckNum, Data))
print("Filter Output : ",FData)

MData = list(map(Increase, FData))
print("Mapped Output : ",MData)

RData = reduce(Product, MData)
print("Reduced Output : ",RData)