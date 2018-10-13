import math

for i in range(101, 201):
    for j in range(2, int(math.log1p(i)) + 2):
        if i % j == 0:
            break
        if j == int(math.log1p(i) + 1):
            print(i)
