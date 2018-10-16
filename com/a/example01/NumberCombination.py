total = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and i != k:
                print(i, end="")
                print(j, end="")
                print(k)
                total += 1
print(total)
#end=""表结尾是什么，默认空格