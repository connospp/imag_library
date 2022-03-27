import unittest
from simple_complex_batch import SimpleComplexBatch
from unittest import TestCase


class TestSimpleComplex(TestCase):
    """This class validates positive test cases against complex library"""
    my_complex_batch = SimpleComplexBatch()

    def test_add_batch_values_one(self):
        """This class validates adding batch of 5 strings"""
        list_of_nums = ["j", "j", "3j", "5j", "-20j"]
        res = self.my_complex_batch.add_complex_list(list_of_nums)  # Parses list
        self.assertEqual("-10j", res)                               # Asserting result

    def test_add_batch_values_two(self):
        """This class validates adding batch of 7 strings"""
        list_of_nums = ["-j", "-j", "-3j", "-5j", "-20j", "j", "25j"]
        res = self.my_complex_batch.add_complex_list(list_of_nums)
        self.assertEqual("-4j", res)

    def test_mult_batch_values_one(self):
        """This class validates multiplying batch of 5 strings"""
        list_of_nums = ["-j", "-j", "-3j", "-5j", "-20j"]
        res = self.my_complex_batch.multiple_complex_list(list_of_nums)
        self.assertEqual("-300j", res)

    def test_mult_batch_values_two(self):
        """This class validates multiplying batch of 6 strings"""
        list_of_nums = ["-2j", "-7j", "-3j", "5j", "-10j", "2j"]
        res = self.my_complex_batch.multiple_complex_list(list_of_nums)
        self.assertEqual("4200j", res)
