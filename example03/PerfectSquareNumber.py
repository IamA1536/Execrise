#这个函数用于判断循环的上限
def work():
    count = 0
    while (count + 1) ** 2 - count ** 2 < 168:
        count += 1
    return count


for i in range(1, work()):
    n = i * i
    if n - 168 - 100 < 0:
        continue
    else:
        if int((n - 168) ** 0.5) < (n - 168) ** 0.5:
            continue
        else:
            print(n - 168 - 100)
