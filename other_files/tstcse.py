from faker import Faker
import random
import string
from datetime import date
import unittest
class FakerAPI(unittest.TestCase):
    def test_negative(self):
        firstValue = "geeks"
        secondValue = "gfg"
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(firstValue, secondValue, message)


if __name__ == '__main__':
    unittest.main()
