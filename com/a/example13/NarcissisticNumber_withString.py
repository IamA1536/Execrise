if __name__ == "__main__":
    for i in range(100, 1000):
        s = str(i)
        a = int(s[-1])
        b = int(s[-2])
        c = int(s[-3])
        if a ** 3 + b ** 3 + c ** 3 == i:
            print(i)
