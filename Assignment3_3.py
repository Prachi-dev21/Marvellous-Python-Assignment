
N = int(input("Enter the number of elements you want to enter in list\n"))

list = []

for i in range(N):
    
    Num = int(input("Enter the Numbers\n"))
    list.append(Num)

min_num = list[0]

for N in list[1:]:
    if N < min_num:
        min_num = N
        
if __name__ == "__main__":

    print("Minimum number from the list is : ", min_num)