

i = 1
sum = 0
def Sum_n(Num):
    global sum, i
    if i <= Num:
        sum = sum + i
        i += 1
        Sum_n(Num)
    return sum

def main():
    N = int(input("Enter the Number: "))
    ret = Sum_n(N)
    print(ret)
   

if __name__ == "__main__":
    main()


    