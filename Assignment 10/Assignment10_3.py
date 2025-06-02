
from functools import reduce 
    
CheckNum = lambda N : (N >= 70 and N <= 90)

Increase = lambda N : N+10

Product = lambda A,B : A*B

Data = [4,34,36,76,68,24,89,23,86,90,45,70]
print("Input Data : ",Data)

FData = list(filter(CheckNum, Data))
print("Filter Output : ",FData)

MData = list(map(Increase, FData))
print("Mapped Output : ",MData)

RData = reduce(Product, MData)
print("Reduced Output : ",RData)