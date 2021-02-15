import unittest
import Conjugado
class TestConjugado(unittest.TestCase):

    def test_div(self):
        self.assertEqual(Conjugado.conjugado("3+5i"),"3-5i")

    def test_div1(self):
        self.assertEqual(Conjugado.conjugado("3-5i"),"3+5i")

    def test_div2(self):
        self.assertEqual(Conjugado.conjugado("-3+5i"),"-3-5i")

    def test_div3(self):
        self.assertEqual(Conjugado.conjugado("-3-5i"),"-3+5i")


if __name__ == "__main__":
    unittest.main()
