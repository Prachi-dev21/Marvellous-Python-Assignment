
i = 1 
 
def Display(n):
    global i
    if i > n:
        return
    print(i, end=" ")
    i += 1
    Display(n)

def main():
    A = int(input("Enter the Number: "))
    Display(A)

if __name__ == "__main__":
    main()
