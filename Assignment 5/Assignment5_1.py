
'''
def Sum(A,B):
    Res =  A+B
    return Res
'''

Sum = lambda A,B : A+B


'''
def Diff(A,B):
    Res =  A-B
    return Res
'''

Diff = lambda A,B : A-B

'''
def Mult(A,B):
    Res =  A*B
    return Res
'''

Mult = lambda A,B : A*B

'''
def Div(A,B):
    Res =  A/B
    return Res
'''

Div = lambda A,B : A/B

if __name__ == "__main__":

    a = int(input("Enter First Number\n"))
    b = int(input("Enter Second Number\n"))

    print("Addition of 2 numbers is : ", Sum(a,b))
    print("Difference of 2 numbers is : ", Diff(a,b))
    print("Multiplicaion of 2 numbers is : ", Mult(a,b))
    print("Division of 2 numbers is : ", Div(a,b))

    