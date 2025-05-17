
def factors(num):
    fact = []
    for i in range(1,num+1):
        if num % i == 0:
            fact.append(i)

    total = 0
    for i in fact:
        total += i

    return total

if __name__ == "__main__":
    num = int(input("Enter the number : "))
    Res = factors(num)
    print(Res)
