import unittest
from car_restrictions import Car
from contextlib import contextmanager
import builtins

@contextmanager
def mockInput(mock):
    orig_input = builtins.input
    builtins.input = lambda _: mock
    yield
    builtins.input = orig_input


class TestCarRestrictions(unittest.TestCase):

    def setUp(self):
        self.car_test = Car()

    def test_plate_validation(self):
        with mockInput('AWD-1253'):
            self.assertEqual(self.car_test.get_plate_validation(), 3)

    def test_date_validation(self):
        with mockInput('15/03/19'):
            self.assertEqual(self.car_test.get_date_validation(), (4, 'Friday'))

    def test_time_validation(self):
        with mockInput('10,31'):
            self.assertEqual(self.car_test.get_time_validation(), 0)

    def test_transit(self):
        result = self.car_test.transit(1, 0, 1)
        self.assertEqual(result, "cannot transit")

        result2 = self.car_test.transit(1, 0, 0)
        self.assertEqual(result2, "can transit")

        result3 = self.car_test.transit(9, 2, 1)
        self.assertEqual(result3, "can transit")


if __name__ == '__main__':

    unittest.main()
