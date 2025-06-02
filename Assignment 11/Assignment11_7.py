i = 1
def pattern(num):
    global i
    if i <= num:
        print(i*"* ", end = "")
        print()
        
        i+=1
        pattern(num)

def main():
    N = int(input("Enter the Number: "))
    pattern(N)
    
   

if __name__ == "__main__":
    main()