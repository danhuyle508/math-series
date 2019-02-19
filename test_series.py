from series import fibonacci
from series import lucas
from series import sum_series

def test_fibonacci():
    actual = fibonacci(4)
    expected = 5
    assert expected == actual

def test_lucas():
    actual = lucas(4)
    expected = 11
    assert expected == actual

def test_sum_series():
    actual = sum_series(4,2,1)
    expected = 11
    assert expected == actual
    
def test_sum_series_no_arguments():
    actual = sum_series(4)
    expected = 5
    assert expected == actual    