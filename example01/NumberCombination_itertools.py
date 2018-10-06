import itertools

total = 0
a = [1, 2, 3, 4]
for i in itertools.permutations(a, 3):
    print(i[0], end="")
    print(i[1], end="")
    print(i[2])
    total += 1
print(total)

#itertools，迭代器，之中有很多方法，其中，permutations是在列表a[]中选n个进行排列，返回元组()
