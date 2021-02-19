import unittest
import SumaMatrices


class TestSumaMatrices(unittest.TestCase):

    def test_SumaMatrices(self):
        self.assertEqual(SumaMatrices.SumaMatrices([["3+2i","2+3i"],["2+1i","1+2i"]]
                        ,[["6+3i","0+0i"],["5+1i","4+0i"]]),
                         [["9 + 5i","2 + 3i"],["7 + 2i","5 + 2i"]])
    def test_SumaMatrices2(self):
        self.assertEqual(SumaMatrices.SumaMatrices([["2+3i","3+2i"],["1+2i","2+1i"]]
                        ,[["6+3i","0+0i"],["5+1i","4+0i"]]),
                         [["8 + 6i","3 + 2i"],["6 + 3i","6 + 1i"]])

if __name__ == "__main__":
    unittest.main()
