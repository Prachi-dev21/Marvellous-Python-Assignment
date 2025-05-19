def CheckEligibility(Age):
    if Age < 18:
        print("Not eligible to vote.")
    else:
        print("Eligible to vote")

if __name__ == "__main__":
    Age = int(input("Enter your age: "))
    CheckEligibility(Age)