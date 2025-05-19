def CheckLarge(N):
    large = 0
    for i in N:
        if i > large:
            large = i
    return large
    

def main(val):
    data = []
    for i in range (val):
        Num = int(input("Enter the numbers : "))
        data.append(Num)
    return CheckLarge(data)

if __name__ == "__main__":
    ret = main(5)
    print("Maximun number is : ",ret)