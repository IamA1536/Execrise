def downprint(a, deep):
    if deep != len(a):
        downprint(a, deep + 1)
        print(a[deep], end=" ")


if __name__ == "__main__":
    a = [i for i in input().split(" ")]
    downprint(a, 0)
