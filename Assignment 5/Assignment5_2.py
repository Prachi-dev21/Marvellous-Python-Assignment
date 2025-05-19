
def Check(value):
    Vowels = ['a','e','i','o','u']
    if value in (Vowels):
        print(f"{value} is Vowels")
    else:
        print(f"{value} is Consonant")

if __name__ == "__main__":
    value = input("Enter the Character\n")
    Check(value)
        
