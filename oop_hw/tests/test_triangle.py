import pytest
from triangle import Triangle


@pytest.mark.parametrize("a, b, c", [(3, "2", 3.0), (4, "2", 3.0)])
def test_set_name(a, b, c):
    figure = Triangle(a, b, c)
    assert figure.set_name() == figure.name


@pytest.mark.parametrize("a, b, c", [(3, "2", 3.0), (4, "2", 3.0)])
def test_set_angles(a, b, c):
    figure = Triangle(a, b, c)
    assert figure.set_angles() == figure.angles


@pytest.mark.parametrize("a, b, c", [(3, "2", 3.0), (4, "2", 3.0)])
def test_set_area(a, b, c):
    figure = Triangle(a, b, c)
    assert figure.set_area() == figure.area


@pytest.mark.parametrize("a, b, c", [(3, "2", 3.0), (4, "2", 3.0)])
def test_set_perimeter(a, b, c):
    figure = Triangle(a, b, c)
    assert figure.set_perimeter() == figure.perimeter
