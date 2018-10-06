pro = int(input("input profit:"))
sum = 0
thresholds = [100000, 100000, 200000, 200000, 400000]
rates = [0.1, 0.075, 0.05, 0.03, 0.01]
for i in range(len(thresholds)):
    if pro <= thresholds[i]:
        sum += pro * rates[i]
        pro = 0
        break
    else:
        sum += thresholds[i] * rates[i]
        pro -= thresholds[i]
sum += pro * rates[-1]
print(sum)
