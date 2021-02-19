import unittest
import ConjugadoMatriz_Vector


class TestConjugadoMatriz_Vector(unittest.TestCase):

    def testConjugadoMatriz_Vector(self):
        self.assertEqual(ConjugadoMatriz_Vector.ConjugadoVector(["2+1i","1+2i"]),["2-1i","1-2i"])
    def testConjugadoMatriz_Vector2(self):
        self.assertEqual(ConjugadoMatriz_Vector.ConjugadoVector(["6+4i","4+6i"]),["6-4i","4-6i"])
    def testConjugadoMatriz_Vector3(self):
        self.assertEqual(ConjugadoMatriz_Vector.ConjugadoVector(["4+2i","2+4i"]),["4-2i","2-4i"])
    def testConjugadoMatriz_Vector4(self):
        self.assertEqual(ConjugadoMatriz_Vector.ConjugadoMatriz([["4+2i","2+4i"],["2+1i","1+2i"]])
                         ,[["4-2i","2-4i"],["2-1i","1-2i"]])
    def testConjugadoMatriz_Vector5(self):
        self.assertEqual(ConjugadoMatriz_Vector.ConjugadoMatriz([["4+2i","2+4i"],["6+4i","4+6i"]])
                         ,[["4-2i","2-4i"],["6-4i","4-6i"]])

if __name__ == "__main__":
    unittest.main()
