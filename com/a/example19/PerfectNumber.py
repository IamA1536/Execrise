if __name__ == "__main__":
    for i in range(6, 1001):
        sum = 0
        for j in range(1, int(i / 2) + 1):
            if i % j == 0:
                sum += j

        if sum == i:
            print(i)
