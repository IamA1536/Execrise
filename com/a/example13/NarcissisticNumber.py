import math

if __name__ == "__main__":
    for i in range(100, 1000):
        a = i % 10
        b = i // 10 % 10
        c = i // 100
        if math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3) == i:
            print(i)
