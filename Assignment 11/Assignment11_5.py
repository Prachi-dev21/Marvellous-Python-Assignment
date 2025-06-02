
count = 0
i = 0
def CountZero(N):
    global count, i
    if i < len(N):
        val = N[i]
        #print ("***val***", val)
        if val == "0":
            count += 1
        i += 1
        CountZero(N)
    return count
    
def main():
    Num = input("Enter the Number: ")
    ret = CountZero(Num)
    print(ret)
   

if __name__ == "__main__":
    main()