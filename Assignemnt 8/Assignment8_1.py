import threading

def Even(n):
    data = []
    count = 1
    x = 0
    while(count <= n):
        x = x+2
        data.append(x)
        count += 1
    print(data)

def Odd(n):
    data = []
    count = 1
    x = 1
    while(count <= n):
       
        data.append(x)
        x = x+2
        count += 1
    print(data)
   
   
def main():

    T1 = threading.Thread(target = Even, args= (10,))
    T2 = threading.Thread(target = Odd, args= (10,))
    
    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
        
        
