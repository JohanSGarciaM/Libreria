import unittest
import InversoAditivo


class TestInversoAditivo(unittest.TestCase):

    def test_InversoAditivo(self):
        self.assertEqual(InversoAditivo.InversoAditivo(["2+2i","3+2i"]),["-2-2i","-3-2i"])

    def test_InversoAditivo2(self):
        self.assertEqual(InversoAditivo.InversoAditivo(["10-28i","4-44i"]),["-10+28i","-4+44i"])

    def test_InversoAditivo3(self):
        self.assertEqual(InversoAditivo.InversoAditivo(["17+43i","23-61i"]),["-17-43i","-23+61i"])

    def test_InversoAditivo4(self):
        self.assertEqual(InversoAditivo.InversoAditivo(["-75-57i","34-45i"]),["75+57i","-34+45i"])


if __name__ == "__main__":
    unittest.main()
