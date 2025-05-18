
def Frequency(N):
    element = int(input("Element to search"))

    count = 0
    for i in (N):
        if element == i:
            count += 1
    return count


def main(A):
    lis = []
    for i in range(A):
        
        Num = int(input("Enter the Numbers\n"))
        lis.append(Num)
    
    return Frequency(lis)


if __name__=="__main__":
    Ans = int(input("Enter the size"))
    ret = main(Ans)
    print("Frequency: ",ret)
    