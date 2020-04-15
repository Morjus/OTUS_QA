import pytest


def test_split():
    test_string = "it is a test string for test"
    test_string_splitted = test_string.split()
    assert type(test_string_splitted) == list, "split() is not worked"


def test_capitalize():
    test_string = "iT iS a TeSt StRiNg fOr TeSt"
    test_string_capitalized = test_string.capitalize()
    assert test_string_capitalized == "It is a test string for test", "capitalize() is not worked"


def test_count():
    test_string = "iT iS a teSt StRiNg fOr TeSt"
    count = test_string.count("teSt")
    assert count == 1, f"{count} is not 1"


def test_replace():
    test_string = "it is a test string for test"
    new_test_string = test_string.replace("test string", "TEST")
    assert new_test_string == "it is a TEST for test", f"{new_test_string} is now equal 'it is a TEST for test'"


@pytest.mark.parametrize("number", [i for i in range(10)])
def test_zfill(number):
    new_num = str(number).zfill(10)
    assert new_num == "000000000" + \
        str(number), f"{new_num} is not equal 000000000{number}"
