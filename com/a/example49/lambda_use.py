MAX = lambda x, y: x * (x >= y) + y * (y > x)
MIN = lambda x, y: x * (x <= y) + y * (y < x)
if __name__ == "__main__":
    a = int(input("Please input the first number:"))
    b = int(input("Please input the second number:"))
    print(MAX(a, b))
    print(MIN(a, b))
