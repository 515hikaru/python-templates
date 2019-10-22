"""
Sample some tests
"""
from python_template import fizzbuzz


def test_fizzbuzz():
    """
    test for fizzbuzz func
    """
    assert fizzbuzz(11) == "11"
    assert fizzbuzz(12) == "fizz"
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(20) == "buzz"
