from figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__(self, a, b)
        self.a = self.check_input(a)
        self.b = self.check_input(b)
        if self.a != self.b:
            self.__name = self.set_name()
            self.__angles = self.set_angles()
            self.__area = self.set_area()
            self.__perimeter = self.set_perimeter()
        else:
            raise Exception(f"That rectangle(first side:{a}, second side{b}) is square!")

    @staticmethod
    def set_name():
        return "Rectangle"

    @staticmethod
    def set_angles():
        return 4

    def set_area(self):
        return self.a*self.b

    def set_perimeter(self):
        return (self.a + self.b)*2

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


cir = Rectangle("2", 3.0)
print(cir.name)
print(cir.angles)
print(cir.area)
print(cir.perimeter)

rect = Rectangle(12, 34)
print(rect.name)
print(rect.angles)
print(rect.area)
print(rect.perimeter)

res = cir.add_square(rect)
print(res)
