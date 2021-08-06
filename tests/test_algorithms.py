import unittest
import algorithms


class TestAlgorithms(unittest.TestCase):

    def test_binary_search(self):
        my_list = [1, 3, 5, 7, 9]

        result = algorithms.binary_search(my_list, 3)
        self.assertEqual(result, 1)

        result = algorithms.binary_search(my_list, -1)
        self.assertIsNone(result)

    def test_selection_sort(self):
        myList = [5, 3, 6, 2, 10]
        result = algorithms.selectionSort(myList)

        self.assertListEqual(result, [2, 3, 5, 6, 10])

    def test_quick_sort(self):
        myList = [5, 3, 6, 2, 10]
        result = algorithms.quicksort(myList)

        self.assertListEqual(result, [2, 3, 5, 6, 10])

    def test_breadth_first_search(self):
        graph = {
            "you": ["alice", "bob", "claire"],
            "bob": ["anuj", "peggy"],
            "alice": ["peggy"],
            "claire": ["thom", "jonny"],
            "peggy": [],
            "anuj": [],
            "thom": [],
            "jonny": [],
        }
        algorithms.breadth_first_search(graph,"you")
