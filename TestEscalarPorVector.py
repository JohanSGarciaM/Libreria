import unittest
import EscalarPorVector


class TestEscalarPorVector(unittest.TestCase):

    def test_EscalarPorVector(self):
        self.assertEqual(EscalarPorVector.EscalarPorVector("3+2i",["6+3i","0+0i","5+1i","4+0i"]),
                         ["12+21i","0+0i","13+13i","12+8i"])
    def test_EscalarPorVector2(self):
        self.assertEqual(EscalarPorVector.EscalarPorVector("1+2i",["3+6i","0+0i","1+5i","0+4i"]),
                         ["-9+12i","0+0i","-9+7i","-8+4i"])
    def test_EscalarPorVector3(self):
        self.assertEqual(EscalarPorVector.EscalarPorVector("2+4i",["1+3i","2+5i","6+2i","4+2i"]),
                         ["-10+10i","-16+18i","4+28i","0+20i"])
    def test_EscalarPorVector4(self):
        self.assertEqual(EscalarPorVector.EscalarPorVector("9+12i",["-9+7i","4+8i","4+7i","2+1i"]),
                         ["-165-45i","-60+120i","-48+111i","6+33i"])


if __name__ == "__main__":
    unittest.main()
