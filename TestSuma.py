import unittest
import Suma


class TestSuma(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(Suma.suma("2+2i", "3+2i"), "5 + 4i")

    def test_sum1(self):
        self.assertEqual(Suma.suma("10-28i", "4-44i"), "14 - 72i")

    def test_sum2(self):
        self.assertEqual(Suma.suma("17+43i", "23-61i"), "40 - 18i")

    def test_sum3(self):
        self.assertEqual(Suma.suma("-75-57i", "34-45i"), "-41 - 102i")

    def test_sum4(self):
        self.assertEqual(Suma.suma("-0+0i", "-0+0i"), "0 + 0i")


if __name__ == "__main__":
    unittest.main()
