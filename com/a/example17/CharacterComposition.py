if __name__ == "__main__":
    str = input("Please input the string: ")
    ccount = 0
    ncount = 0
    spacecount = 0
    ocount = 0
    for i in str:
        if i.isalpha():
            ccount += 1
        elif i.isdigit():
            ncount += 1
        elif i.isspace():
            spacecount += 1
        else:
            ocount += 1
    print("The number of letter is {0}.".format(ccount))
    print("The number of number is {0}.".format(ncount))
    print("The number of spacebar is {0}.".format(spacecount))
    print("The number of others is {0}.".format(ocount))
