import unittest
import lambdas


class TestLambdas(unittest.TestCase):
    def setUp(self):
        self.myFunction = lambdas.myFunction
        self.myOtherFunction = lambdas.myOtherFunction
        self.sum_two_nums = lambdas.sum_two_nums
        self.subtract_two_nums = lambdas.subtract_two_nums
        self.l_string = "<lambda>"

    def test_myFunction(self):

        self.assertTrue(self.myFunction.__name__ == self.l_string)

    def test_myOtherFunction(self):
        self.assertTrue(self.myOtherFunction.__name__ == self.l_string)

    def test_sum_two_nums(self):
        self.assertTrue(self.sum_two_nums.__name__ == self.l_string)
        expeted = 3
        actual = self.sum_two_nums(1, 2)

        self.assertEqual(expeted, actual)

    def test_subtract_two_nums(self):
        self.assertTrue(self.subtract_two_nums.__name__ == self.l_string)
        expected = 0
        actual = self.subtract_two_nums(4, 4)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
