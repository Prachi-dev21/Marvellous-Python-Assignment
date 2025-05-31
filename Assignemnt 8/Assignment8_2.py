import threading

def Evenfactor(n):
    total = 0
    factors = []
    for i in range(2, n+1 , 2):
        if n % i == 0:
            total += i
    print(f"Sum of even factors is: {total}")


def Oddfactor(n):
    total = 0
    factors = []
    for i in range(1, n+1 , 2):
        if n % i == 0:
            total += i
    print(f"Sum of odd factors is: {total}")



def main():
    
    num = int(input("Enter a positive integer: "))

    T1 =threading.Thread(target = Evenfactor, args = (num,))
    T2 =threading.Thread(target = Oddfactor, args = (num,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()
    
    print("Exit from main")

if __name__ == "__main__":

    main()