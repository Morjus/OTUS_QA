import pytest
from square import Square


@pytest.mark.parametrize("side", [1, "2", 3.0, "4.0"])
def test_set_name(side):
    figure = Square(side)
    assert figure.set_name() == figure.name


@pytest.mark.parametrize("side", [1, "2", 3.0, "4.0"])
def test_set_angles(side):
    figure = Square(side)
    assert figure.set_angles() == figure.angles


@pytest.mark.parametrize("side", [1, "2", 3.0, "4.0"])
def test_set_area(side):
    figure = Square(side)
    assert figure.set_area() == figure.area


@pytest.mark.parametrize("side", [1, "2", 3.0, "4.0"])
def test_set_perimeter(side):
    figure = Square(side)
    assert figure.set_perimeter() == figure.perimeter

