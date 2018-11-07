if __name__ == "__main__":
    lettert = {"h": "thursday",
               "u": "tuesday"}
    letters = {"a": "saturday",
               "u": "sunday"}
    letter0 = {"m": "monday",
               "w": "wensday",
               "f": "friday",
               "t": lettert,
               "s": letters}
    a = letter0[input().lower()]
    if a == letters or a == lettert:
        print(a[input("Need the second: ").lower()])
    else:
        print(a)
