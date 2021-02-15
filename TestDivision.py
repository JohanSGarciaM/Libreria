import unittest
import Division


class TestDivision(unittest.TestCase):

    def test_div(self):
        self.assertEqual(Division.division("-4+5i","8-2i"), "-0.62 + 0.47i")

    def test_div1(self):
        self.assertEqual(Division.division("1+2i","3-4i"), "-0.2 + 0.4i")

    def test_div2(self):
        self.assertEqual(Division.division("2-2i","3+4i"), "-0.08 - 0.56i")

    def test_div3(self):
        self.assertEqual(Division.division("5+2i","-3-4i"), "-0.92 + 0.56i")


if __name__ == "__main__":
    unittest.main()
