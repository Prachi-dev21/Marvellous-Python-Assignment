def Even():
    add = 0
    for i in range(1,101):
        if i % 2 == 0:
            add += i
    return add

if __name__=="__main__":

    print("Sum of all even numbers is", Even())