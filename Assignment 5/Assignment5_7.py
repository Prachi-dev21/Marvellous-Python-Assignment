
def Area(l,w):
    a = l*w
    return a

def Perimeter(l,w):
    p = 2*(l+w)
    return p

if __name__ == "__main__":

    l = int(input("Enter the length of the rectangle : \n"))
    w = int(input("Enter the width of the rectangle : \n"))
    
    area = Area(l,w) 
    perimeter = Perimeter(l,w) 

    print("Area of Rectangle:", area)
    print("Perimeter of Rectangle:", perimeter)
