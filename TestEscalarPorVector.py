import unittest
import EscalarPorVector


class TestEscalarPorVector(unittest.TestCase):

    def test_EscalarPorVector(self):
        self.assertEqual(EscalarPorVector.EscalarPorVector(3,["6+3i","0+0i","5+1i","4+0i"]),
                         ["18+9i","0+0i","15+3i","12+0i"])
    def test_EscalarPorVector2(self):
        self.assertEqual(EscalarPorVector.EscalarPorVector(2,["3+6i","0+0i","1+5i","0+4i"]),
                         ["6+12i","0+0i","2+10i","0+8i"])
    def test_EscalarPorVector3(self):
        self.assertEqual(EscalarPorVector.EscalarPorVector(4,["1+3i","2+5i","6+2i","4+2i"]),
                         ["4+12i","8+20i","24+8i","16+8i"])
    def test_EscalarPorVector4(self):
        self.assertEqual(EscalarPorVector.EscalarPorVector(9,["1+7i","4+8i","4+7i","2+1i"]),
                         ["9+63i","36+72i","36+63i","18+9i"])


if __name__ == "__main__":
    unittest.main()
