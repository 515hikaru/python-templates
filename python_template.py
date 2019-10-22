"""
Awesome package
"""

__version__ = "1.0.2"


def fizzbuzz(num):
    """
    fizzbuzz logic
    """
    ret = ""
    if num % 3 == 0:
        ret += "fizz"
    if num % 5 == 0:
        ret += "buzz"
    if ret == "":
        return str(num)
    return ret


def main():
    """main routine"""
    for i in range(100):
        val = fizzbuzz(i)
        print(i, val)
