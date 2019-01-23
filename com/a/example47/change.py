def exchange(a, b):
    return (b, a)


if __name__ == "__main__":
    a = int(input("Please input the first number:"))
    b = int(input("Please input the second number:"))
    a, b = exchange(a, b)
    print(a)
    print(b)
