def Palindrome(a):
    
    return a == a[::-1]        
    
if __name__ == "__main__":

    A = input("Enter the String\n")
    
    if Palindrome(A):
        print(f"{A} is a palindrome")
    else:
        print(f"{A} is not a palindrome")