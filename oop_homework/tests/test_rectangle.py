import pytest
from rectangle import Rectangle


@pytest.mark.parametrize("a, b", [(3, "2"), (2, 3.0)])
def test_set_name(a, b):
    figure = Rectangle(a, b)
    assert figure.set_name() == figure.name


@pytest.mark.parametrize("a, b", [(3, "2"), (2, 3.0)])
def test_set_angles(a, b):
    figure = Rectangle(a, b)
    assert figure.set_angles() == figure.angles


@pytest.mark.parametrize("a, b", [(3, "2"), (2, 3.0)])
def test_set_area(a, b):
    figure = Rectangle(a, b)
    assert figure.set_area() == figure.area


@pytest.mark.parametrize("a, b", [(3, "2"), (2, 3.0)])
def test_set_perimeter(a, b):
    figure = Rectangle(a, b)
    assert figure.set_perimeter() == figure.perimeter

