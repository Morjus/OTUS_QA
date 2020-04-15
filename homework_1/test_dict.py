import pytest


def test_clear():
    test_dict = {"john": 23, "thom": 65, "jimmy": 54}
    test_dict.clear()
    assert len(test_dict) == 0, f"{test_dict} is not empty!"


def test_values():
    test_dict = {"john": 23, "thom": 65, "jimmy": 54}
    list_from_values = list(test_dict.values())
    assert list_from_values == [
        23, 65, 54], f"{list_from_values} is not correct!"


def test_pop():
    test_dict = {"john": 23, "thom": 65, "jimmy": 54}
    pop_john = test_dict.pop("john")
    assert pop_john not in test_dict, f"{pop_john} is in {test_dict}!"


@pytest.mark.parametrize("name", ["john", "thom", "jimmy"])
def test_setdefault(name):
    test_dict = {"mike": 23}
    test_dict.setdefault(name)
    assert test_dict[name] == None, f"{test_dict[name]} is not None!"


def test_update():
    test_dict_1 = {"john": 23, "thom": 65, "jimmy": 54}
    test_dict_2 = {"monica": 45, "jen": 38, "alice": 19}
    test_dict_1.update(test_dict_2)
    assert len(test_dict_1) == 6, f"{test_dict_2} is not in {test_dict_1}"
