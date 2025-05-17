from MarvellousNum import CheckPrime # type: ignore

from functools import reduce

def ListPrime(N):
    nums = []   
    for i in range(N):

        number = int(input("Enter the Numbers\n"))
        nums.append(number)
    print ("Numbers",nums)
    return nums
    

def Add(A,B):
    return A+B

N = int(input("Enter the number of elements you want to enter in list\n"))
nums = ListPrime(N)

result = []
for number in nums:    
    if CheckPrime(number):
        result.append(number)

print("Result is : ",result)

if result:
    Res = reduce(Add, result)
else:
    Res = 0

print("The Sum of numbers is : ", Res)