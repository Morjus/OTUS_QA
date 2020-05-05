import pytest
from circle import Circle


@pytest.mark.parametrize("radius", [1, "2", 3.0, "4.0"])
def test_set_name(radius):
    figure = Circle(radius)
    assert figure.set_name() == figure.name


@pytest.mark.parametrize("radius", [1, "2", 3.0, "4.0"])
def test_set_angles(radius):
    figure = Circle(radius)
    assert figure.set_angles() == figure.angles


@pytest.mark.parametrize("radius", [1, "2", 3.0, "4.0"])
def test_set_area(radius):
    figure = Circle(radius)
    assert figure.set_area == figure.area


@pytest.mark.parametrize("radius", [1, "2", 3.0, "4.0"])
def test_set_perimeter(radius):
    figure = Circle(radius)
    assert figure.set_perimeter == figure.perimeter
