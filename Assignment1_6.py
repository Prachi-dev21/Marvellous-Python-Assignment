def check_Num(num):
    if num > 0:
        num_is = "Positive Number"
    elif num <0:
        num_is = "Negative Number"
    else:
        num_is = "Zero"

    return num_is

if __name__ == "__main__":

    Number = float(input("Enter your number : "))

    result = check_Num(Number)
    print(result)
