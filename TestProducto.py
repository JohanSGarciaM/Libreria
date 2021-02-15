import unittest
import producto


class TestMultiplicacion(unittest.TestCase):

    def test_mult(self):
        self.assertEqual(producto.producto("2+2i","2+4i"), "-4 + 12i")

    def test_mult1(self):
        self.assertEqual(producto.producto("15-28i","24-44i"), "-872 - 1332i")

    def test_mult2(self):
        self.assertEqual(producto.producto("78+26i","27-98i"), "4654 - 6942i")

    def test_mult3(self):
        self.assertEqual(producto.producto("-100-1i", "-9-8i"), "892 + 809i")

    def test_mult4(self):
        self.assertEqual(producto.producto("-0+0i", "-0+0i"), "0 + 0i")


if __name__ == "__main__":
    unittest.main()
