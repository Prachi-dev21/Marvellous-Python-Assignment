
def Table(N):
    for i in range(1, 11):
        print(f"{N} * {i} = {N * i}")

if __name__ == "__main__":
    num = int(input("Enter the Number\n"))
    Table(num)
