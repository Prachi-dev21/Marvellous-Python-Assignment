import threading

def Small(s):
    count = 0
    for i in s:
        
        if i.islower():
            count += 1
    print("Small Letters :", count)

def Capital(s):
    count = 0
    for i in s:
        
        if i.isupper():
            count += 1
    print("Capital Letters :", count)

def Digit(s):
    count = 0
    for i in s:
        
        if i.isdigit():
            count += 1
    print("Number of digits :", count)

def main():

    ABC = input("Enter the string : ")

    t1 = threading.Thread(target = Small, args=(ABC,))
    t2 = threading.Thread(target = Capital, args=(ABC,))
    t3 = threading.Thread(target = Digit, args=(ABC,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()
