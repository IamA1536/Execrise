if __name__ == "__main__":
    str = input()
    i = 0
    j = len(str) - 1
    while i < j:
        if str[i] != str[j]:
            break
        i += 1
        j -= 1
    if i >= j:
        print("True")
    else:
        print("False")
