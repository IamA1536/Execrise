def work(n):
    if n <= 2:
        return 1
    else:
        sum = work(n - 1) + work(n - 2)
        return sum


n = int(input("Please input the number of Sequence:"))
for i in range(1, n + 1):
    print(work(i), end=" ")
