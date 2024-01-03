from centro.central import version_dados
import unittest

class TestJuego(unittest.TestCase):
    
    def test_v0_num_enteros(self):
        result = version_dados()
        self.assertTrue(isinstance(result, tuple))
        self.assertEqual(len(result), 2)

        dado1, dado2 = result
        self.assertTrue(1 <= dado1 <= 6, )
        self.assertTrue(1 <= dado2 <= 6, )
        result = version_dados("Demo","3")
        self.assertEquals(result)

    def test_suma_dados(self):
        result = version_dados()
        suma = sum(result)
        self.assertTrue(2 <= suma <= 12,)
        
    def test_dados(self):
        flag = True
        while(flag == True):
            i += 1
        if i == 13:
            flag = False
            i = version_dados("Demo","5")
        
    

if __name__ == '__main__':
    unittest.main()



