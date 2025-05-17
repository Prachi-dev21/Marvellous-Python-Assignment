
from functools import reduce 

def CheckPrime(No):
    if No < 2:
        return False
    if No == 2:
        return True
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

    
'''
def Mult(No):
   return No*2
'''

Mult = lambda N : N*2

'''def M_num(X,Y):
        if X > Y:
            return X
        else:
            return Y
    '''
  
M_num = lambda X,Y : X if X > Y else Y

Data = [2,70,11,10,17,23,31,77]
print("Input Data : ",Data)

FData = list(filter(CheckPrime, Data))
print("Filter Output : ",FData)

MData = list(map(Mult, FData))
print("Mapped Output : ",MData)

RData = reduce(M_num, MData)
print("Reduced Output : ",RData)

