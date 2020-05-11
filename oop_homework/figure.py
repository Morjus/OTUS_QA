class Figure:


    def __init__(self, a=None, b=None, c=None, r=None):
        self.__name = None
        self.__angles = None
        self.__area = None
        self.__perimeter = None

        self.a = a
        self.b = b
        self.c = c
        self.r = r
        # self.a = self.check_input(a)
        # self.b = self.check_input(b)
        # self.c = self.check_input(c)
        # self.r = self.check_input(r)

    def check_input(self, arg):
        if self.is_integer(arg):
            return self.is_integer(arg)
        elif self.is_float(arg):
            return self.is_float(arg)
        else:
            raise Exception(f'{arg} is not integer or float.')

    @classmethod
    def is_float(cls, arg):
        try:
            arg = float(arg)
            return arg
        except (ValueError, TypeError):
            pass

    @staticmethod
    def is_integer(arg):
        try:
            arg = int(arg)
            return arg
        except (ValueError, TypeError):
            pass

    def add_square(self, another_class):
        return self.area + another_class.area

