import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):
    
    def test_total_returns_total_of_list(self):

        result = Grades.total([1, 10,22])
        self.assertEqual(result, 33, 'The total function should return 33')


    def test_total_returns_0(self):
        
        result = Grades.total([])
        self.assertEqual(result, 0, 'The total function should return 0')

    def test_average_one(self):

        result = Grades.average([2, 5, 9])
        self.assertAlmostEqual(result, 5.3333, 4, 'The average function should return 5.3333') 

    def test_average_two(self):

        result = Grades.average([2, 15, 22, 9])
        self.assertAlmostEqual(result, 12, 4, 'The average function should return 12') 

    def test_average_returns_nan(self):

        result = Grades.average([])
        self.assertIs(math.nan, result, 'The average function should return nan') 

    def test_median_one(self):
        '''Test for median when list has an odd amount of numbers'''

        result = Grades.median([2, 5, 1])
        self.assertEqual(result, 2, 'The median function should return 2')

    def test_median_two(self):
        '''Test for median when list has an event amount of numbers'''

        result = Grades.median([5, 2, 1, 3])
        self.assertEqual(result, 2.5, 'The median function should return 2.5')

    def test_median_three(self):
        '''Test that median returns a ValueError when an empty is passed'''

        with self.assertRaises(ValueError):
            result = Grades.median([])

unittest.main()

