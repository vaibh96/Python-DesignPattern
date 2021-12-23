class Test:

    data_one = 222
    def __init__(self, name):
        self.printMessage(name)
        self.__number = 122
        pass

    def getData(self):
        return self.__number

    def printMessage(self, name):
        print(name)

    @staticmethod
    def staticMethod():
        print("Im static method")

    def accessclassvar(cls):
        print("classs variable value is {}".format(cls.data_one))

    def __str__(self):
        return "Object Test "


if __name__ == '__main__':
    t1 = Test("vaibhav")
    t2 = Test("Gole")
    print(t1.staticMethod())
    print(Test.staticMethod())
    print(t1.accessclassvar())
