"""
Testing EightDieClass methods that return a testable value.
"""

import random
import unittest

from TwelveDie import TwelveDieClass
from EightDie import EightDieClass


class TestEightDieClass(unittest.TestCase):
    def setUp(self):
        """
        Sets up two EightDieClass objects,
        a positive one with all attributes set and blank negative
        :return: EightDieClass
        """
        self.nobj = EightDieClass(False)
        self.pobj = EightDieClass(True)
        self.pobj.set_symbol1("Success")
        self.pobj.set_symbol2("")
        self.pobj.set_symbol3("Advantage")
        self.pobj.set_isdouble(True)

    def test_get_sides(self):
        # Ensures both objects have 8 sides
        self.assertEqual(self.nobj.get_sides(), 8)
        self.assertEqual(self.pobj.get_sides(), 8)

    def test_get_positive(self):
        # Ensures that the negative object is negative
        self.assertEqual(self.nobj.get_positive(), False)
        # Ensures that the positive object is positive
        self.assertEqual(self.pobj.get_positive(), True)

    def test_set_positive(self):
        # Set negative obj to positive then assert the change went through
        self.nobj.set_positive(True)
        self.assertEqual(self.nobj.get_positive(), True)

        # Set positive obj to wrong value to assert default is False
        self.pobj.set_positive(1)
        self.assertEqual(self.pobj.get_positive(), False)

    def test_get_symbol1(self):
        # Check that positive obj symbol1 is correct
        self.assertEqual(self.pobj.get_symbol1(), "Success")

    def test_set_symbol1(self):
        # Set negative symbol one to Failure and assert the value was passed
        self.nobj.set_symbol1("Failure")
        self.assertEqual(self.nobj.get_symbol1(), "Failure")

    def test_get_symbol2(self):
        # Check that positive obj symbol2 is correct
        self.assertEqual(self.pobj.get_symbol2(), "")

    def test_set_symbol2(self):
        # Set negative symbol one to Despair and assert the value was passed
        self.nobj.set_symbol2("Despair")
        self.assertEqual(self.nobj.get_symbol2(), "Despair")

    def test_get_symbol3(self):
        # Check that positive obj symbol3 is correct
        self.assertEqual(self.pobj.get_symbol3(), "Advantage")

    def test_set_symbol3(self):
        # Set negative symbol one to Threat and assert the value was passed
        self.nobj.set_symbol3("Threat")
        self.assertEqual(self.nobj.get_symbol3(), "Threat")

    def test_get_isdouble(self):
        # Assert that positive object is double and negative is not
        self.assertEqual(self.nobj.get_isdouble(), False)
        self.assertEqual(self.pobj.get_isdouble(), True)

    def test_set_isdouble(self):
        # Set negative object to be double and assert the value was changed
        self.nobj.set_isdouble(True)
        self.assertEqual(self.nobj.get_isdouble(), True)

    def test_is_blank(self):
        # Assert that nobj is blank
        self.assertEqual(self.nobj.is_blank(), True)
        # Assert that pobj is not blank
        self.assertEqual(self.pobj.is_blank(), False)

    def test_cancel(self):
        # Create instance of the wrong class
        fool = TwelveDieClass()
        # Assert that passing it raises an error
        with self.assertRaises(ArithmeticError):
            self.nobj.cancel(fool)

    def test_Nroll1(self):
        # Change seed to one that results in a 1 roll
        random.seed(2)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 1
        self.assertEqual(result, 1)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), False)
        self.assertEqual(self.nobj.get_symbol1(), "")
        self.assertEqual(self.nobj.get_symbol3(), "Threat")
        self.assertEqual(self.nobj.get_isdouble(), False)

    def test_Proll1(self):
        # Change seed to one that results in a 1 roll
        random.seed(2)

        # Change to positive
        self.nobj.set_positive(True)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 1
        self.assertEqual(result, 1)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), True)
        self.assertEqual(self.nobj.get_symbol1(), "")
        self.assertEqual(self.nobj.get_symbol3(), "Advantage")
        self.assertEqual(self.nobj.get_isdouble(), False)

    def test_Nroll2(self):
        # Change seed to one that results in a 2 roll
        random.seed(6)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 2
        self.assertEqual(result, 2)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), False)
        self.assertEqual(self.nobj.get_symbol3(), "")
        self.assertEqual(self.nobj.get_symbol1(), "Failure")
        self.assertEqual(self.nobj.get_isdouble(), False)

    def test_Proll2(self):
        # Change seed to one that results in a 1 roll
        random.seed(6)

        # Change to positive
        self.nobj.set_positive(True)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 2
        self.assertEqual(result, 2)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), True)
        self.assertEqual(self.nobj.get_symbol1(), "Success")
        self.assertEqual(self.nobj.get_symbol3(), "")
        self.assertEqual(self.nobj.get_isdouble(), False)

    def test_Nroll3(self):
        # Change seed to one that results in a 3 roll
        random.seed(33)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 3
        self.assertEqual(result, 3)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), False)
        self.assertEqual(self.nobj.get_symbol3(), "Threat")
        self.assertEqual(self.nobj.get_symbol1(), "")
        self.assertEqual(self.nobj.get_isdouble(), False)

    def test_Proll3(self):
        # Change seed to one that results in a 3 roll
        random.seed(33)

        # Change to positive
        self.nobj.set_positive(True)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 3
        self.assertEqual(result, 3)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), True)
        self.assertEqual(self.nobj.get_symbol1(), "")
        self.assertEqual(self.nobj.get_symbol3(), "Advantage")
        self.assertEqual(self.nobj.get_isdouble(), True)

    def test_Nroll4(self):
        # Change seed to one that results in a 4 roll
        random.seed(4)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 4
        self.assertEqual(result, 4)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), False)
        self.assertEqual(self.nobj.get_symbol3(), "Threat")
        self.assertEqual(self.nobj.get_symbol1(), "")
        self.assertEqual(self.nobj.get_isdouble(), False)

    def test_Proll4(self):
        # Change seed to one that results in a 4 roll
        random.seed(4)

        # Change to positive
        self.nobj.set_positive(True)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 4
        self.assertEqual(result, 4)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), True)
        self.assertEqual(self.nobj.get_symbol1(), "Success")
        self.assertEqual(self.nobj.get_symbol3(), "Advantage")
        self.assertEqual(self.nobj.get_isdouble(), False)

    def test_Nroll5(self):
        # Change seed to one that results in a 5 roll
        random.seed(13)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 5
        self.assertEqual(result, 5)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), False)
        self.assertEqual(self.nobj.get_symbol3(), "")
        self.assertEqual(self.nobj.get_symbol1(), "Failure")
        self.assertEqual(self.nobj.get_isdouble(), True)

    def test_Proll5(self):
        # Change seed to one that results in a 5 roll
        random.seed(13)

        # Change to positive
        self.nobj.set_positive(True)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 5
        self.assertEqual(result, 5)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), True)
        self.assertEqual(self.nobj.get_symbol1(), "")
        self.assertEqual(self.nobj.get_symbol3(), "Advantage")
        self.assertEqual(self.nobj.get_isdouble(), False)

    def test_Nroll6(self):
        # Change seed to one that results in a 6 roll
        random.seed(7)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 6
        self.assertEqual(result, 6)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), False)
        self.assertEqual(self.nobj.get_symbol3(), "Threat")
        self.assertEqual(self.nobj.get_symbol1(), "")
        self.assertEqual(self.nobj.get_isdouble(), True)

    def test_Proll6(self):
        # Change seed to one that results in a 1 roll
        random.seed(7)

        # Change to positive
        self.nobj.set_positive(True)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 6
        self.assertEqual(result, 6)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), True)
        self.assertEqual(self.nobj.get_symbol1(), "")
        self.assertEqual(self.nobj.get_symbol3(), "Advantage")
        self.assertEqual(self.nobj.get_isdouble(), False)

    def test_Nroll7(self):
        # Change seed to one that results in a 7 roll
        random.seed(17)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 7
        self.assertEqual(result, 7)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), False)
        self.assertEqual(self.nobj.get_symbol3(), "Threat")
        self.assertEqual(self.nobj.get_symbol1(), "Failure")
        self.assertEqual(self.nobj.get_isdouble(), False)

    def test_Proll7(self):
        # Change seed to one that results in a 7 roll
        random.seed(17)

        # Change to positive
        self.nobj.set_positive(True)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 7
        self.assertEqual(result, 7)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), True)
        self.assertEqual(self.nobj.get_symbol1(), "Success")
        self.assertEqual(self.nobj.get_symbol3(), "")
        self.assertEqual(self.nobj.get_isdouble(), True)

    def test_Nroll8(self):
        # Change seed to one that results in an 8 roll
        random.seed(11)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 8
        self.assertEqual(result, 8)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), False)
        self.assertEqual(self.nobj.get_symbol3(), "")
        self.assertEqual(self.nobj.get_symbol1(), "")
        self.assertEqual(self.nobj.get_isdouble(), False)

    def test_Proll8(self):
        # Change seed to one that results in an 8 roll
        random.seed(11)

        # Change to positive
        self.nobj.set_positive(True)

        # Record rolled number
        result = self.nobj.roll()

        # Assert that it rolled 8
        self.assertEqual(result, 8)

        # Check if the face values are correct
        self.assertEqual(self.nobj.get_positive(), True)
        self.assertEqual(self.nobj.get_symbol1(), "")
        self.assertEqual(self.nobj.get_symbol3(), "")
        self.assertEqual(self.nobj.get_isdouble(), False)
