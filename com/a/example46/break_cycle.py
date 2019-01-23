if __name__ == "__main__":
    while True:
        n = int(input("Please input a number: "))
        if n ** 2 > 50:
            print("It is too large!")
            break
        else:
            print(n ** 2)
