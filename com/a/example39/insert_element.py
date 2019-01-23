if __name__ == "__main__":
    a = [int(i) for i in input().split(" ")]
    b = int(input("Please input a number: "))
    a.append(b)
    if a[0] < a[len(a) // 2]:
        a.sort(reverse=False)
    else:
        a.sort(reverse=True)
    print(a)
