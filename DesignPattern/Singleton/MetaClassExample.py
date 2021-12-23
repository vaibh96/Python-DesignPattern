class D(type):

    def __call__(cls, *args, **kwargs):
        instance = super(D, cls).__call__(*args, **kwargs)
        return instance

    def __init__(cls, name, base, attr):
        super(D, cls).__init__(name, base, attr)


class E(metaclass=D):
    pass

print(D)
