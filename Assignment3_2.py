
N = int(input("Enter the number of elements you want to enter in list\n"))

list = []

for i in range(N):
    
    Num = int(input("Enter the Numbers\n"))
    list.append(Num)

max_num = list[0]

for N in list[1:]:
    if N > max_num:
        max_num = N

print("Maximum number from the list is : ", max_num) 