sum = 0
while sum != -1:
    pro = int(input("input profit："))
    if pro < 0:
        break
    sum = 0
    if pro > 100000:
        sum += 100000 * 0.1
        if pro > 200000:
            sum += 100000 * 0.075
            if pro > 400000:
                sum += 200000 * 0.05
                if pro > 600000:
                    sum += 20000 * 0.03
                    if pro > 1000000:
                        sum += 400000 * 0.015
                        sum += (pro - 1000000) * 0.01
                    else:
                        sum += (pro - 600000) * 0.015
                else:
                    sum += (pro - 400000) * 0.03
            else:
                sum += (pro - 200000) * 0.05
        else:
            sum += (pro - 100000) * 0.075
    else:
        sum += pro * 0.1
    print(sum)
