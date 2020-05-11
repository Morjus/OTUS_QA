import math
from figure import Figure


class Circle(Figure):
    def __init__(self, r):
        super().__init__(self, r)
        self.r = self.check_input(r)
        if self.r:
            self.__name = self.set_name()
            self.__angles = self.set_angles()
            self.__area = self.set_area
            self.__perimeter = self.set_perimeter
        else:
            raise Exception("That Circle is not exists!")

    @staticmethod
    def set_name():
        return "Circle"

    @staticmethod
    def set_angles():
        return 0

    @property
    def set_area(self):
        return (self.r**2)*math.pi

    @property
    def set_perimeter(self):
        return 2*self.r*math.pi

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





# cir = Circle("3.0")
# print(cir.name)
# print(cir.angles)
# print(cir.area)
# print(cir.perimeter)
# cir = Circle("3")
# print(cir.name)
# print(cir.angles)
# print(cir.area)
# print(cir.perimeter)
# cir = Circle(3.0)
# print(cir.name)
# print(cir.angles)
# print(cir.area)
# print(cir.perimeter)
# cir = Circle(3)
# print(cir.name)
# print(cir.angles)
# print(cir.area)
# print(cir.perimeter)
