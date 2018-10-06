n = int(input("Please input the number of Sequence:"))
s = [1, 1]
if n == 1:
    print(1)
else:
    if n == 2:
        print(1, 1)
    else:
        print(1, end=" ")
        for i in range(2, n + 1):
            t = s[1]
            s[1] += s[0]
            s[0] = t
            print(s[0], end=" ")
