global num


class Dummy:
    num: int = 1

    def num(self):
        print('class dummy num:', self.num)
        print('global num: ', num)
        self.num += 1


if __name__ == "__main__":
    n = Dummy()
    num = 1
    for i in range(5):
        num *= 10
        n.num()
