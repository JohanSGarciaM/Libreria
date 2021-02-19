import unittest
import InversaAditivaMatriz


class TestInversaAditivaMatriz(unittest.TestCase):

    def test_InversaAditivaMatriz(self):
        self.assertEqual(InversaAditivaMatriz.InversaAditivaMatriz([["3+2i","2+3i"],["2+1i","1+2i"]]),
                         [["-3-2i","-2-3i"],["-2-1i","-1-2i"]])
    def test_InversaAditivaMatriz2(self):
        self.assertEqual(InversaAditivaMatriz.InversaAditivaMatriz([["2+3i","3+2i"],["1+2i","2+1i"]]),
                         [["-2-3i","-3-2i"],["-1-2i","-2-1i"]])
    def test_InversaAditivaMatriz4(self):
        self.assertEqual(InversaAditivaMatriz.InversaAditivaMatriz([["8+6i","3+2i"],["6+3i","6+1i"]]),
                         [["-8-6i","-3-2i"],["-6-3i","-6-1i"]])



if __name__ == "__main__":
    unittest.main()
