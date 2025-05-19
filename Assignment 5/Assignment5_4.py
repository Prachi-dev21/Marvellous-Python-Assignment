
def Large(N1,N2,N3):
    if N1 > N2:
        if N1 > N3:
            Largest = N1
    elif N2 > N1:
        if N2 > N3:
            Largest = N2
        else:
            Largest = N3

    return Largest

if __name__ == "__main__":
    N1 = int(input("Enter the Number1\n"))
    N2 = int(input("Enter the Number2\n"))
    N3 = int(input("Enter the Number3\n"))
    Res = Large(N1,N2,N3)
    print(Res)