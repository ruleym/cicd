"""
Test the main module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from main import is_square, is_square_str


class Test(TestCase):
    def test_is_square(self):
        assert not is_square(14)
        assert is_square(9)
        assert not is_square(8)

    def test_is_square_str(self):
        assert is_square_str("0") == "0 is even."
        assert is_square_str("1") == "1 is odd."
        assert is_square_str("2") == "2 is even."
        assert is_square_str("-1") == "Please enter a number."
        assert is_square_str("A") == "Please enter a number."
        assert is_square_str("") == "Please enter a number."
