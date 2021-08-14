"""This module implements test cases for the written program and directly
for the NumberFormatter class using the Python unit testing framework.
"""

import unittest
import number_formatter


class TestNumberFormatterMethods(unittest.TestCase):

    def setUp(self):
        self.TestNumberFormatter = number_formatter.NumberFormatter()

    def test_common_result(self):
        self.assertEqual(self.TestNumberFormatter.parseInt('3682916'), 3682916)

    def test_positive_result(self):
        self.assertEqual(self.TestNumberFormatter.parseInt('+274911859987'), 274911859987)

    def test_negative_result(self):
        self.assertEqual(self.TestNumberFormatter.parseInt('-668289188'), -668289188)

    def test_string_starts_at_null(self):
        self.assertEqual(self.TestNumberFormatter.parseInt('000000271819'), 271819)

    def test_raise_length_exception(self):
        self.assertRaises(Exception, self.TestNumberFormatter.parseInt, '1')

    def test_raise_type_exception(self):
        self.assertRaises(TypeError, self.TestNumberFormatter.parseInt, [1, 2, 3])



if __name__ == '__main__':
    unittest.main()
