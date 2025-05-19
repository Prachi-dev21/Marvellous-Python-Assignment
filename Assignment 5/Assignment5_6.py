
def CtoF(Temp):
    F = (Temp * (9/5)) + 32

    return F
    
if __name__ == "__main__":
    Temperature = int(input("Enter the temperature in Celcius\n"))
    Ans = CtoF(Temperature)
    print("Temperature in Fahrenheit : ", Ans ,"F")

