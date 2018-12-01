if __name__ == "__main__":
    a = [1, 2, 3]
    strl = ""
    for i in a:
        strl += str(i) + ","
    print(strl[:-1])
