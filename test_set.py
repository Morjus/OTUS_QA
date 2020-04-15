import pytest


def test_add():
    test_set = set()
    test_set.add(1)
    test_set.add(1)
    test_set.add(1)
    assert len(test_set) == 1, f"In {test_set} is not one element!"


def test_union():
    test_set_1 = {"orange", "pinapple", "grape"}
    test_set_2 = {"orange", "pinapple", "banana"}
    test_set_3 = test_set_1.union(test_set_2)
    assert len(test_set_3) == 4, f"In {test_set_3} more than 4 elements!"


@pytest.mark.parametrize("fruit", ["banana", "lemon", "grape"])
def test_discard(fruit):
    test_set = {"orange", "pinapple", "grape"}
    #discard_data = "orange"
    test_set.discard(fruit)
    assert fruit not in test_set, f"{fruit} in {test_set}!"


def test_difference():
    test_set_1 = {"orange", "pinapple", "grape"}
    test_set_2 = {"orange", "lemon", "grape"}
    test_set_3 = test_set_1.difference(test_set_2)
    assert test_set_3 == {
        "pinapple"}, f"In {test_set_3} wrong difference between 1 set and 2 set!"


def test_copy():
    test_set_1 = {"orange", "pinapple", "grape"}
    test_set_2 = test_set_1.copy()
    assert id(test_set_1) != id(
        test_set_2), f"{test_set_2} and {test_set_2} are same object!"
