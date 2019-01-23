def comparison(a, b):
    if a > b:
        return (b, a)
    else:
        return (a, b)


if __name__ == "__main__":
    a = int(input("Please input the first number:"))
    b = int(input("Please input the second number:"))
    a, b = comparison(a, b)
    print(str(a) + " < " + str(b))
