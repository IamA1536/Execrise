if __name__ == "__main__":
    for i in range(4):
        for j in range(3 - i):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()
    for i in range(3):
        for j in range(i + 1):
            print(" ", end="")
        for j in range(2 * (3 - i) - 1):
            print("*", end="")
        print()
