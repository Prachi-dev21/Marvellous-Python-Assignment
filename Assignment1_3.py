
def Add(Num1,Num2):

    Res = Num1 + Num2
    
    return Res

if __name__=='__main__':
    
    val1 = int(input("Enter 1st Number\n"))
    val2 = int(input("Enter 2nd Number\n"))
    Res = Add(val1,val2)
    print("Addition\n",Res)
    