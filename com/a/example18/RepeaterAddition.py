import copy
import math

if __name__ == "__main__":
    s = input("Please input the number: ")
    n = int(input("Please input the time of adding: "))
    num = copy.deepcopy(s)
    sum = 0

    for i in range(n):
        sum += int(num)
        num += s

    print("The result is {0}.".format(sum))
