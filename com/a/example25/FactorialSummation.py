def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


if __name__ == "__main__":
    sum = 0
    for i in range(1, 20):
        sum += factorial(i)
    print(sum)
