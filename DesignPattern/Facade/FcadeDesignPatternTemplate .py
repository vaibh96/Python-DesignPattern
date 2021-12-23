class Smoke(object):
    def __init__(self):
        pass

    def smokeOn(self):
        print("Smoke is On")

    def smokeOFF(self):
        print("Smoke is OFF")


class Lights(object):
    def __init__(self):
        pass

    def LightsOn(self):
        print("Smoke is On")

    def LightsOFF(self):
        print("Smoke is OFF")


class Desktop(object):
    def __init__(self):
        pass

    def DesktopOn(self):
        print("Smoke is On")

    def DesktopOFF(self):
        print("Smoke is OFF")


class MetaClass(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        """create instance at once """

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class Facade(metaclass=MetaClass):

    def __init__(self):
        self._smoke = Smoke()
        self._lights = Lights()
        self._desktop = Desktop()

    def Emergency(self):
        self._smoke.smokeOFF()
        self._lights.LightsOFF()
        self._desktop.DesktopOFF()

    def NoEmergency(self):
        self._smoke.smokeOn()
        self._lights.LightsOn()
        self._desktop.DesktopOn()


if __name__ == '__main__':
    obj = Facade()
    print(obj)
    obj2 = Facade()
    print(obj2)
    smoke = 80

    if smoke > 60:
        obj.Emergency()
    else:
        obj.NoEmergency()


