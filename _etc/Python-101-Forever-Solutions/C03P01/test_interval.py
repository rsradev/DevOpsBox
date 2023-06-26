from interval import Interval
from unittest import TestCase
#Test suite
class IntervalTests(TestCase):
    ##test case
    def test_string_produces_correct_result(self):
        interval = Interval(1,10)
        excepted = "[1, 10]"

        self.assertEqual(excepted, str(interval))

    def test_is_inside_produces_corrrect_results(self):
        interval = Interval(1,21)

        self.assertTrue(interval.is_inside(1))
        self.assertTrue(interval.is_inside(5))
        self.assertTrue(interval.is_inside(19))





