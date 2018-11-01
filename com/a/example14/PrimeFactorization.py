import math

if __name__ == "__main__":
    n = int(input("Please input a number: "))
    if n < 0:
        print(-1, end=" ")
        n = abs(n)
    while n != 1:
        if math.ceil(math.log(n)) > 2:
            for i in range(2, math.ceil(math.log(n)) + 1):
                if n % i == 0:
                    n = n // i
                    print(i, end=" ")
                    break
                if i == math.ceil(math.log(n)):
                    print(n, end=" ")
                    n = 1
                    break
        else:
            if i != 4 and i != 6:
                print(n, " ")
                break
