import unittest
import AdicionVectores

class TestAdicionVectores(unittest.TestCase):
    def test_sum1(self):
        self.assertEqual(AdicionVectores.adicionVectores(["6-4i","7+3i","42-81i","1+1i"],["16+23i","1-7i","6+0i","0-4i"])
                         ,['22 + 19i', '8 - 4i', '48 - 81i', '1 - 3i'])
    def test_sum2(self):
        self.assertEqual(AdicionVectores.adicionVectores(["4+5i","1+2i","2-1i"],["3+2i","5+3i","2+1i"]),["7 + 7i","6 + 5i","4 + 0i"])

    def test_sum3(self):
        self.assertEqual(AdicionVectores.adicionVectores(["14+7i","3+6i","3-6i"],["13+21i","15+6i","6+7i"]),["27 + 28i","18 + 12i","9 + 1i"])

    def test_sum4(self):
        self.assertEqual(AdicionVectores.adicionVectores(["5+4i","2+1i","1-2i"],["2+3i","3+5i","1+2i"]),["7 + 7i","5 + 6i","2 + 0i"])

    def test_sum5(self):
        self.assertEqual(AdicionVectores.adicionVectores(["7+7i","6+5i","4-0i"],["3+2i","5+3i","2+1i"]),["10 + 9i","11 + 8i","6 + 1i"])
if __name__== "__main__":
    unittest.main()
