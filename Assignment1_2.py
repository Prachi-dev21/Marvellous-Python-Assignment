

def ChkNum(number):
        
    if number%2 == 0:
        res = "Even Number"
    else:
        res = "Odd Number"

    return res
    
if __name__ == "__main__":

    val = int(input("Enter Number"))
    ans = ChkNum(val)
    print(ans)
    