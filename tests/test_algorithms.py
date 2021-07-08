import unittest
import algorithms


class TestAlgorithms(unittest.TestCase):

    def test_binary_search(self):
        my_list = [1, 3, 5, 7, 9]

        result = algorithms.binary_search(my_list, 3)
        print(result)
        self.assertEqual(result, 1)
