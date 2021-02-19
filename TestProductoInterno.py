import unittest
import ProductoInterno


class TestProductoInterno(unittest.TestCase):

    def test_ProductoInterno(self):
        self.assertEqual(ProductoInterno.ProductoInterno(["18+9i","0+0i","15+3i","12+0i"],["6+3i","0+0i","5+1i","4+0i"]),"201+138i")
    def test_ProductoInterno2(self):
        self.assertEqual(ProductoInterno.ProductoInterno(["3+6i","0+0i","1+5i","0+4i"],["6+12i","0+0i","2+10i","0+8i"]),"-134+92i")
    def test_ProductoInterno3(self):
        self.assertEqual(ProductoInterno.ProductoInterno(["1+3i","2+5i","6+2i","4+2i"],["4+12i","8+20i","24+8i","16+8i"]),"60+264i")
    def test_ProductoInterno4(self):
        self.assertEqual(ProductoInterno.ProductoInterno(["1+7i","4+8i","4+7i","2+1i"],["9+63i","36+72i","36+63i","18+9i"]),"-1134+1242i")


if __name__ == "__main__":
    unittest.main()
