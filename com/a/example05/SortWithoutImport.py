print("Please input three numbers:", end="")
n = [int(i) for i in input().split(" ")]
for i in range(3):
    for j in range(2):
        if n[j] > n[j + 1]:
            t = n[j]
            n[j] = n[j + 1]
            n[j + 1] = t
print(n)
