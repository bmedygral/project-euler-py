from p2 import fibb, sum_of_even_fibb



def test_f1bb():
    assert list(fibb(1)) == [1]
    assert list(fibb(2)) == [1, 2]
    assert list(fibb(5)) == [1, 2, 3, 5]

def test_sum_of_even_fibb():
    assert sum_of_even_fibb(5) == 2