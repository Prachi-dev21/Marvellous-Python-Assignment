import multiprocessing

def Square(N):
    List = []
    for i in N:
        List.append(i*i)
    print(List)


def main():

    #numbers = [1, 2, 3, 4, 5]
    numbers = list(map(int,input().split()))
    t1 = multiprocessing.Process(target= Square, args=(numbers,))

    t1.start()
    t1.join()
    
if __name__ == "__main__":
    
    main() 