def rec(deep):
    if deep == 0:
        return 10
    else:
        return rec(deep - 1) + 2


if __name__ == "__main__":
    print(rec(4))
