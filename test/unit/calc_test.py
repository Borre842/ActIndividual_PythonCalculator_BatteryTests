import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    #Test batteries for Add
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
    
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    #Test Batteries for substract
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(2, 2))
        self.assertEqual(0, self.calc.substract(2, -2))
        self.assertEqual(0, self.calc.substract(-2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))
    
    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    #Test batteries for divide
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    
    #Test batteries for multiply
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertEqual(-2, self.calc.multiply(0, 0))

    #Test Batteries for log10
    def test_log10_method_fails_with_data(self):
        #postive
        self.assertRaises(TypeError, self.calc.log10, 100)
        #one
        self.assertRaises(TypeError, self.calc.log10, 1)
        #float
        self.assertRaises(TypeError, self.calc.log10, 0.01)
        #zero
        self.assertRaises(TypeError, self.calc.log10, 0)
        #negative
        self.assertRaises(TypeError, self.calc.log10, -1)
        #string
        self.assertRaises(TypeError, self.calc.log10, "10")

    #Test for batteries for Square
    def test_square_method_failes_with_data(self):
        #postive
        self.assertRaises(TypeError, self.calc.square, 16)
        #negative
        self.assertRaises(TypeError, self.calc.square, -16)
        #zero
        self.assertRaises(TypeError, self.calc.square, 0)
        #float
        self.assertRaises(TypeError, self.calc.square, 8.29)
        #large
        self.assertRaises(TypeError, self.calc.square, 1000000000000)
        #one
        self.assertRaises(TypeError, self.calc.square, 1)
        #string
        self.assertRaises(TypeError, self.calc.square, "16")

    #Test for batteries fro power
    def test_power_method_failes_with_data(self):
        #positive
        self.assertRaises(TypeError, self.calc.power, 2 , 3)
        #negative
        self.assertRaises(TypeError, self.calc.power, -2 , 3)
        #negative exponent
        self.assertRaises(TypeError, self.calc.power, 2 , -3)
        #zero
        self.assertRaises(TypeError, self.calc.power, 0 , 1)
        #zero exponent
        self.assertRaises(TypeError, self.calc.power, 2 , 0)
        #zero both
        self.assertRaises(TypeError, self.calc.power, 0 , 0)
        #float
        self.assertRaises(TypeError, self.calc.power, 2.5 , 3)
        #float exponent
        self.assertRaises(TypeError, self.calc.power, 2 , 3.5)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
