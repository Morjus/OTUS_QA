from figure import Figure


class Square(Figure):
    def __init__(self, a):
        super().__init__(self, a)
        self.a = self.check_input(a)
        if self.a:
            self.__name = self.set_name()
            self.__angles = self.set_angles()
            self.__area = self.set_area()
            self.__perimeter = self.set_perimeter()
        else:
            raise Exception("That square is not exists!")

    def set_name(self):
        if self.a:
            return "Square"

    def set_angles(self):
        if self.a:
            return 4

    def set_area(self):
        if self.a:
            return self.a*self.a

    def set_perimeter(self):
        if self.a:
            return self.a * self.angles

    @property
    def name(self):
        return self.__name

    @property
    def angles(self):
        return self.__angles

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter
