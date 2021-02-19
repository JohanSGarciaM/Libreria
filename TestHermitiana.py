import unittest
import Hermitiana


class TestHermitiana(unittest.TestCase):

    def test_Hermitiana(self):
        self.assertTrue(Hermitiana.Hermitiana([["5+0i","3+7i"],["3-7i","2+0i"]]))
    def test_Hermitiana2(self):
        self.assertTrue(Hermitiana.Hermitiana([["3+0i","2-1i","0-5i"],["2+1i","0+0i","9-5i"],["0+5i","9+5i","6+0i"]]))
    def test_hermitiana3(self):
        self.assertTrue(Hermitiana.Hermitiana([["2+0i","1+1i","9+2i","0+0i"],["1-1i","5+0i","4+6i","3-2i"],["9-2i","4-6i","10+0i","1+7i"],["0+0i","3+2i","1-7i","4+0i"]]))
    


if __name__ == "__main__":
    unittest.main()
