
import Arithmetic


def main(N1,N2):
    Addition_is = Arithmetic.Add(N1,N2)
    print("Addition of two numbers is : ",Addition_is)

    Subtraction_is = Arithmetic.Sub(N1,N2)
    print("Subtraction of two numbers is : ",Subtraction_is)

    Multiplication_is = Arithmetic.Mult(N1,N2)
    print("Multiplication of two numbers is : ",Multiplication_is)

    Division_is = Arithmetic.Div(N1,N2)
    print("Division of two numbers is : ",Division_is)


if __name__ == '__main__':
    
    a = int(input("Enter 1st Number\n"))
    b = int(input("Enter 2nd Number\n"))

    Res = main(a,b)





