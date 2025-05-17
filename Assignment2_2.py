
def Star(n):
    for i in range(n):
        
        count = 1
        while count <= n:
            print("*", end = " ")
            count += 1
        print()


if __name__ == '__main__':

    a = int(input("Enter number\n"))
    Size = Star(a)



    
