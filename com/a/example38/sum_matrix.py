def sum_matrix(a):
    print(a[0][0] + a[0][2] + a[1][1] + a[2][0] + a[2][2])


if __name__ == "__main__":
    a = []
    for i in range(3):
        b = [int(j) for j in input().split()]
        b = b[:3]
        a.append(b)
    sum_matrix(a)
