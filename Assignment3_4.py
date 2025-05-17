
N = int(input("Enter the number of elements you want to enter in list\n"))

lis = []

for i in range(N):
    
    Num = int(input("Enter the Numbers\n"))
    lis.append(Num)

max_num = lis[0]

for N in lis[1:]:
    if N > max_num:
        max_num = N

print("Maximun number from the list is : ", max_num)