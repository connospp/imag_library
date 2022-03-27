import unittest
from simple_complex import SimpleComplex
from simple_complex_batch import SimpleComplexBatch

from unittest import TestCase


class TestSimpleComplex(TestCase):
    """This class validates negative test cases against complex library"""
    my_complex = SimpleComplex()
    my_complex_batch = SimpleComplexBatch()

    def test_wrong_value_one(self):
        """Verifies more characters after j are being detected as invalid"""
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex.add_complex("3jas", "2j")  # Call function with 1 valid 1 invalid number
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, ValueError,f"Expected {ValueError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_value_two(self):
        """Verifies string ending in more than 1 j is being detected as invalid"""
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex.add_complex("-3jj", "j", "2j")
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, ValueError,f"Expected {ValueError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_value_three(self):
        """Verifies more js are being detected as invalid"""
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex.sub_complex("j3j", "2j")
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, ValueError,f"Expected {ValueError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_value_four(self):
        """Verifies double - sign is being detected as invalid"""
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex.sub_complex("--3j", "2j")
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, ValueError,f"Expected {ValueError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_value_five(self):
        """Verifies double + sign is being detected as invalid"""
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex.multiple_complex("++3j", "2j")
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, ValueError,f"Expected {ValueError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_value_six(self):
        """Verifies starting with letter is being detected as invalid"""
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex.multiple_complex("q3j", "-j", "2j")
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, ValueError,f"Expected {ValueError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_value_seven(self):
        """Verifies real numbers are not allowed"""
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex.divide_complex("1", "-j")
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, ValueError,f"Expected {ValueError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_value_eight(self):
        """Verifies generic string not allowed"""
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex.divide_complex("no_number", "-j")
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, ValueError,f"Expected {ValueError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_value_nine(self):
        """Verifies empty string not allowed"""
        list_of_numbers = ["", "-j"]
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex_batch.add_complex_list(list_of_numbers)
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, ValueError,f"Expected {ValueError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_value_ten(self):
        """Verifies special characters not allowed"""
        list_of_numbers = ["-j", "-j", "%$£"]
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex_batch.multiple_complex_list(list_of_numbers)
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, ValueError,f"Expected {ValueError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_value_elev(self):
        """Verifies whitespace character not allowed"""
        list_of_numbers = [" ", "-j", "-3j"]
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex_batch.multiple_complex_list(list_of_numbers)
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, ValueError,f"Expected {ValueError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_type_one(self):
        """Verifies None type is not allowed"""
        list_of_numbers = [None, "-j", "-3j"]
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex_batch.multiple_complex_list(list_of_numbers)
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, AttributeError,f"Expected {AttributeError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised

    def test_wrong_type_two(self):
        """Verifies int type is not allowed"""
        list_of_numbers = [3, "-j", "-3j"]
        ex_type = None
        res = "no_result_returned"
        try:
            res = self.my_complex_batch.multiple_complex_list(list_of_numbers)
        except Exception as e:
            ex_type = type(e)

        self.assertEqual(ex_type, AttributeError,f"Expected {AttributeError} but instead got {ex_type}. Result came back as: {res}")  # Verifies exemption raised
