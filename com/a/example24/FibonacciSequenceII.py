if __name__ == "__main__":
    a = 2.0
    b = 1.0
    s = 0
    for i in range(1, 21):
        s += a / b
        a, b = a + b, a
    print(s)
