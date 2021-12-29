
class meta(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(meta, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class Person(metaclass=meta):

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        pass

    def display(self):
        print("Name is {}".format(self.name))
        print("Phone Number is {}".format(self.phone_number))


class Employee(Person):

    def __init__(self, name, phone_number, city):
        self.name = name
        self.phone_number = phone_number
        self.city = city
        Person.__init__(self, name, phone_number)

    def show(self):
        print("City is {}".format(self.city))


if __name__ == "__main__":
    p1 = Employee(name='vaibhav', phone_number=9383737883, city='Pune')
    p1.show()
    p1.display()
    print(type(Employee))
    p2 = Employee()
    print(p2)
