"""

Factory Design pattern

"""


class A(object):
    def __init__(self):
        pass

    def print(self):
        print("Class A")


class B(object):

    def __init__(self):
        pass

    def print(self):
        print("Class B")


def get(obj=''):
    objs = dict(a=A(), b=B())
    return objs[obj]


a = get('a')
a.print()

b = get('b')
b.print()
