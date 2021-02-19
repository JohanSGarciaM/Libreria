import unittest
import InversaAditivaMatriz


class TestInversaAditivaMatriz(unittest.TestCase):

    def test_InversaAditivaMatriz(self):
        self.assertEqual(InversaAditivaMatriz.InversaAditivaMatriz([["3+2i","0+0i","5-6i"],["1+0i","4+2i","0+1i"],["4-1i","0+0i","4+0i"]]),
                         [["-3-2i","0+0i","-5+6i"],["-1+0i","-4-2i","0-1i"],["-4+1i","0+0i","-4+0i"]])
    def test_InversaAditivaMatriz2(self):
        self.assertEqual(InversaAditivaMatriz.InversaAditivaMatriz([["26-52i","60+24i","26+0i"],["9+7i","1+29i","14+0i"],["48-21i","15+22i","20-22i"]]),
                         [["-26+52i","-60-24i","-26+0i"],["-9-7i","-1-29i","-14+0i"],["-48+21i","-15-22i","-20+22i"]])
    
    def test_InversaAditivaMatriz3(self):
        self.assertEqual(InversaAditivaMatriz.InversaAditivaMatriz([["2+3i","3+2i"],["1+2i","2+1i"]]),[["-2-3i","-3-2i"],["-1-2i","-2-1i"]])
    def test_InversaAditivaMatriz4(self):
        self.assertEqual(InversaAditivaMatriz.InversaAditivaMatriz([["8+6i","3+2i"],["6+3i","6+1i"]]),[["-8-6i","-3-2i"],["-6-3i","-6-1i"]])



if __name__ == "__main__":
    unittest.main()
