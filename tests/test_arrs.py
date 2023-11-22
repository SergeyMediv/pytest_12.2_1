from utils import arrs


def test_get(one_two_three):
    assert arrs.get(one_two_three, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(one_two_three):
    assert arrs.my_slice(one_two_three, 1, 3) == [2, 3]
    assert arrs.my_slice(one_two_three, 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(one_two_three, None, 3) == [1, 2, 3]
