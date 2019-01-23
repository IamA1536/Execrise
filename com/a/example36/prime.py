import math


def prime(n):
    # print(math.ceil(math.sqrt(n)))
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        else:
            continue
    return True


if __name__ == "__main__":
    print(2, end=" ")
    for i in range(3, 98):
        if prime(i):
            print(i, end=" ")
