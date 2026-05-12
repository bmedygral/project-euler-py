from p1 import multiples_of_n, sum_of_multiples_of_ns


def test_multiples_of_n():
    assert list(multiples_of_n(3, 10)) == [3, 6, 9]


def test_sum_of_multiples_of_ns():
    assert sum_of_multiples_of_ns([3, 5], 10) == 23
