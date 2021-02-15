import unittest
import Resta


class TestResta(unittest.TestCase):

    def test_res(self):
        self.assertEqual(Resta.resta("14-2i","-3+2i"), "17 - 4i")

    def test_res1(self):
        self.assertEqual(Resta.resta("7+2i", "5-9i"), "2 + 11i")

    def test_res2(self):
        self.assertEqual(Resta.resta("78+26i", "27-98i"), "51 + 124i")

    def test_res3(self):
        self.assertEqual(Resta.resta("-100-1i", "-9-8i"), "-91 + 7i")

    def test_res4(self):
        self.assertEqual(Resta.resta("-0+0i", "-0+0i"), "0 + 0i")


if __name__ == "__main__":
    unittest.main()
