from figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__(self, a, b, c)
        self.a = self.check_input(a)
        self.b = self.check_input(b)
        self.c = self.check_input(c)
        # Проверка существования треугольника
        if self.a + self.b > self.c \
                and self.a + self.c > self.b \
                and self.b + self.c > self.a:
            self.__name = self.set_name()
            self.__angles = self.set_angles()
            self.__perimeter = self.set_perimeter()
            self.__area = self.set_area()
        else:
            raise Exception("That triangle is not exists!")

    @staticmethod
    def set_name():
        return "Triangle"

    @staticmethod
    def set_angles():
        return 3

    def set_perimeter(self):
        return self.a + self.b + self.c

    def set_area(self):
        if self.a and self.b and self.c:
            p = self.set_perimeter()
            s = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
            return s

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

# cir = Triangle("2",2.0,"3.1")
# print(cir.name)
# print(cir.angles)
# print(cir.area)
# print(cir.perimeter)