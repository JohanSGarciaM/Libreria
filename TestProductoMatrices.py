import unittest
import ProductoMatrices


class TestProductoMatrices(unittest.TestCase):

    def test_ProductoMatrices(self):
        self.assertEqual(ProductoMatrices.ProductoMatrices([["3+2i","0+0i","5-6i"],["1+0i","4+2i","0+1i"],["4-1i","0+0i","4+0i"]],
                           [["5+0i","2-1i","6-4i"],["0+0i","4+5i","2+0i"],["7-4i","2+7i","0+0i"]]),
                         [['26-52i', '60+24i', '26+0i'], ['9+7i', '1+29i', '14+0i'], ['48-21i', '15+22i', '20-22i']])
    def test_ProductoMatrices2(self):
        self.assertEqual(ProductoMatrices.ProductoMatrices([["2+3i","3+2i"],["1+2i","2+1i"]],[["-2-3i","-3+2i"],["-1-2i","-2-1i"]]),
                         [["6-20i","-16-12i"],["4-12i","-10-8i"]])
    def test_ProductoMatrices3(self):
        self.assertEqual(ProductoMatrices.ProductoMatrices([["8+6i","3+2i"],["6+3i","6+1i"]],[["-8-6i","-3-2i"],["-6-3i","-6-1i"]]),
                         [["-40-117i","-28-49i"],["-63-84i","-47-33i"]])



if __name__ == "__main__":
    unittest.main()
