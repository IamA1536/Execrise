class Student:
    __id: int
    __name: str

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def print_info(self):
        print("The student " + self.__name + ", the id is " + str(self.__id))

    def __del__(self):
        print("Delete successfully")


if __name__ == "__main__":
    stu1 = Student(1, "A")
    stu2 = Student(2, "B")
    print(stu1.getId())
    print(stu1.getName())
    print(stu2.getId())
    print(stu2.getName())
    stu1.setId(3)
    print(stu1.getId())
    stu1.print_info()
