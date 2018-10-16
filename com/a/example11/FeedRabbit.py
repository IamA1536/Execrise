a = 2
b = 0
n = int(input("Please input the number of month: "))
sum = 0;
count = 0;
m = 0
print("初始，兔子数：0")
for i in range(1, n+1):
    m += 1
    count += 1
    if count == 3:
        a += b
        sum += a // 2
        b = a // 2
        count = 0
    print("第{0}月，兔子数:{1}".format(m, a + b))
