import unittest
from simple_complex import SimpleComplex
from unittest import TestCase


class TestSimpleComplex(TestCase):
    """This class validates positive test cases against complex library"""
    my_complex = SimpleComplex()

    def test_add_two_different_values(self):
        """This class validates adding two strings"""
        res = self.my_complex.add_complex("3j", "2j")  # Parses strings
        self.assertEqual("5j",res)                     # Asserting result

    def test_add_three_different_values(self):
        """This class validates adding three strings"""
        res = self.my_complex.add_complex("-3j", "j","2j")
        self.assertEqual("0j",res)

    def test_sub_two_different_values_first(self):
        """This class validates subtracting two strings"""
        res = self.my_complex.sub_complex("-5j", "2j")
        self.assertEqual("-7j", res)

    def test_sub_two_different_values_second(self):
        """This class validates capital "J" accepted"""
        res = self.my_complex.sub_complex("5j", "2j")
        self.assertEqual("3j", res)

    def test_mult_two_different_values(self):
        """This class validates multiplying two strings"""
        res = self.my_complex.multiple_complex("3j", "2j")
        self.assertEqual("6j",res)

    def test_mult_three_different_values(self):
        """This class validates multiplying three strings"""
        res = self.my_complex.multiple_complex("3j", "-j","2j")
        self.assertEqual("-6j",res)

    def test_div_two_different_values_first(self):
        """This class validates dividing two strings"""
        res = self.my_complex.divide_complex("-6j", "2j")
        self.assertEqual("-3.0j", res)

    def test_div_two_different_values_second(self):
        """This class validates dividing two strings"""
        res = self.my_complex.divide_complex("7j", "2j")
        self.assertEqual("3.5j", res)


