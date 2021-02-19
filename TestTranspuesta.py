import unittest
import Transpuesta


class TestTranspuesta(unittest.TestCase):

    def test_Transpuesta(self):
        self.assertEqual(Transpuesta.TranspuestaVector(["1+6i","2+5i","3+4i","4-3i","5-2i","6+1i"]),
                         [["1+6i"],["2+5i"],["3+4i"],["4-3i"],["5-2i"],["6+1i"]])
    def test_Transpuesta2(self):
        self.assertEqual(Transpuesta.TranspuestaVector(["4+1i","3+2i","2-3i","1-4i"]),[["4+1i"],["3+2i"],["2-3i"],["1-4i"]])
    def test_Transpuesta3(self):
        self.assertEqual(Transpuesta.TranspuestaMatriz([["3+2i","2+3i"],["2+1i","1+2i"]]),[["3+2i","2+1i"],["2+3i","1+2i"]])
    def test_Transpuesta4(self):
        self.assertEqual(Transpuesta.TranspuestaMatriz([["6+3i","0+0i"],["5+1i","4+0i"],["2+3i","3+2i"]]),[["6+3i","5+1i","2+3i"],
                                                    ["0+0i","4+0i","3+2i"]])


if __name__ == "__main__":
    unittest.main()
