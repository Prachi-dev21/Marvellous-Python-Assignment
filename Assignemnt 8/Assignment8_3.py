import threading


def Evenlist(no):
    total = 0
    for num in no:
        if num % 2 == 0:
            total += num
    print(total)

def Oddlist(no):
    total = 0
    for num in no:
        if num % 2 != 0:
            total += num
    print(total)

def main():
    
    List = []
    
    List = list(map(int, input("Enter the numbers: ").split()))

    T1 =threading.Thread(target = Evenlist, args = (List,))
    T2 =threading.Thread(target = Oddlist, args = (List,))
    

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()