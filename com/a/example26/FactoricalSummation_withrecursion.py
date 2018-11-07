def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    sum = 0
    for i in range(1, 20):
        sum += factorial(i)
    print(sum)
