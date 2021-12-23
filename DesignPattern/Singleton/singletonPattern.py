class MetaClass(type):
    """ Singleton Design Pattern  """

    _instance = {}

    def __call__(cls, *args, **kwargs):
        """ if instance already exist dont create one  """

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class Test(metaclass=MetaClass):
    def __init__(self):
        pass

    def method(self):
        print("da")

    def __str__(self):
        return "Instance of the class"


if __name__ == "__main__":
    te = Test()
    te.method()
 
