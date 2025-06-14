def main():
    
    file = open("numbers.txt", 'w')

   
    print("Enter 10 numbers:")
    for i in range(1, 11):
        print(i, end=" ")
        num = input()
        file.write(num + '\n')
   
    file.close()

    print("All numbers written to 'numbers.txt'")

if __name__ == "__main__":
    main()
