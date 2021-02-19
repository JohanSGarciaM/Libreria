import unittest
import Adjunta


class TestAdjunta(unittest.TestCase):

    def test_Adjunta(self):
        self.assertEqual(Adjunta.AdjuntaVector(["1+6i","2+5i","3+4i","4-3i","5-2i","6+1i"]),
                         [["1-6i"],["2-5i"],["3-4i"],["4+3i"],["5+2i"],["6-1i"]])
    def test_Adjunta2(self):
        self.assertEqual(Adjunta.AdjuntaVector(["4+1i","3+2i","2-3i","1-4i"]),[["4-1i"],["3-2i"],["2+3i"],["1+4i"]])
    def test_Adjunta3(self):
        self.assertEqual(Adjunta.AdjuntaMatriz([["3+2i","2+3i"],["2+1i","1+2i"]]),[["3-2i","2-1i"],["2-3i","1-2i"]])
    def test_Adjunta4(self):
        self.assertEqual(Adjunta.AdjuntaMatriz([["6+3i","2+2i"],["5+1i","4+2i"],["2+3i","3+2i"]]),[["6-3i","5-1i","2-3i"],
                                                    ["2-2i","4-2i","3-2i"]])


if __name__ == "__main__":
    unittest.main()
