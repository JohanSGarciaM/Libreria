import unittest
import EscalarPorMatriz


class TestEscalarPorMatriz(unittest.TestCase):

    def test_EscalarPorMatriz(self):
        self.assertEqual(EscalarPorMatriz.EscalarPorMatriz(2,[["3+2i","2+3i"],["2+1i","1+2i"]]),
                         [["6+4i","4+6i"],["4+2i","2+4i"]])
    def test_EscalarPorMatriz2(self):
        self.assertEqual(EscalarPorMatriz.EscalarPorMatriz(3,[["2+3i","3+2i"],["1+2i","2+1i"]]),
                         [["6+9i","9+6i"],["3+6i","6+3i"]])
    def test_EscalarPorMatriz4(self):
        self.assertEqual(EscalarPorMatriz.EscalarPorMatriz(4,[["8+6i","3+2i"],["6+3i","6+1i"]]),
                         [["32+24i","12+8i"],["24+12i","24+4i"]])



if __name__ == "__main__":
    unittest.main()
