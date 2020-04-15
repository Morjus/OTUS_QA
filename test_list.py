import pytest
import random


def test_append():
    test_list = []
    test_list.append("test_element")
    assert len(test_list) == 1, f"{test_list} is empty!"


def test_extend():
    test_list_1 = [0, 1, 2, 3]
    test_list_2 = [4, 5, 6, 7]
    test_list_1.extend(test_list_2)
    assert test_list_1 == [0, 1, 2, 3, 4, 5, 6,
                           7], f"{test_list_1} is not extended with {test_list_2}!"


def test_insert():
    test_list = [0, 1, 2, 3]
    insert_data = -1
    test_list.insert(0, insert_data)
    assert test_list[0] == - \
        1, f"First element '{test_list[0]}' is not equal insert data: {insert_data}!"


def test_remove():
    test_list = [0, 1, 2, 3]
    data_to_remove = 2
    test_list.remove(data_to_remove)
    assert not data_to_remove in test_list, f"{data_to_remove} is in {test_list}!"


@pytest.mark.parametrize('random_number', random.sample(range(0, 10), 10))
def test_count(random_number):
    test_list = [i for i in range(0,10)]
    assert test_list.count(
        random_number) == 1, f"{random_number} is not in {test_list}!"
