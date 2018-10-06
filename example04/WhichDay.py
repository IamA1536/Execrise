def check(n):
    if n % 4 == 0 and n % 100 != 0:
        return 29
    return 28


y = int(input("Please input the year:"))
m = int(input("Please input the mouth:"))
d = int(input("Please input the day:"))
num = [31, check(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum = 0
for i in range(0, m - 1):
    sum += num[i]
sum += d
print("The number of day is %d" % sum)
#print("The number of day is {0}".format(sum))
