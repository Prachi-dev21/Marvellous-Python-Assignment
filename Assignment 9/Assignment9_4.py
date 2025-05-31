import time
import threading
import multiprocessing

def Sum():
    total = 0
    for i in range(1, 10_000_001):
        total += i
    return total

def Sum1():
    start = time.time()
    Sum()
    print("Normal function took:", time.time() - start, "seconds")

def Sum2():
    start = time.time()
    t = threading.Thread(target=Sum)
    t.start()
    t.join()
    print("Threading took:", time.time() - start, "seconds")

def main():
    start = time.time()
    p = multiprocessing.Process(target=Sum)
    p.start()
    p.join()
    print("Multiprocessing took:", time.time() - start, "seconds")

if __name__ == "__main__":
   
    Sum1()
    Sum2()
    main()