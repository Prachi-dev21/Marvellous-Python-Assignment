import threading
import time

def Numbers():
    for i in range(1,6):
        print(i, end=" ")
        time.sleep(1)
    print()
    

def main():

    t1 = threading.Thread(target= Numbers)
    t2 = threading.Thread(target= Numbers)
    t3 = threading.Thread(target= Numbers)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()
    
if __name__ == "__main__":
    main()