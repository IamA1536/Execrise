def sum_matrix(a, b, n):
    for i in range(n):
        for j in range(n):
            a[i][j] = a[i][j] + b[i][j]
    return a


if __name__ == "__main__":
    n = int(input("Please input the number: "))
    a = []
    b = []
    print("Please input the first matrix:")
    for i in range(n):
        c = [int(j) for j in input().split(" ")]
        a.append(c[:n])
    print("Please input the second matrix:")
    for i in range(n):
        c = [int(j) for j in input().split(" ")]
        b.append(c[:n])
    print(sum_matrix(a, b, n))
