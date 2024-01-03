import unittest
from programas.combinacion import combinacion
class Test_combinacion(unittest.TestCase):
    

    def test_combi(self):
        n = 9
        r = 5
        area = combinacion(n,r)
        self.assertEquals(area,1)
        
    def test_combinacion_floats(self):
        r = 4.5
        n = 2

        with self.assertRaises(ValueError) as exc:
          combinacion(r,n)
        self.assertEqual(str(exc.exception),'no admite decimales')

    def test_combinacion_n_invalida(self):
        n = 'Hola'
        r = 5
         
        with self.assertRaises(ValueError) as exc:
            combinacion(n,r)
        
        self.assertEqual(str(exc.exception),'debe ser numerico')
    
    def test_combinacion_negativa(self):
        r = -2
        n = -1
         
        with self.assertRaises(ValueError) as exc:
            combinacion(r,n)
        
        self.assertEqual(str(exc.exception),'debe ser un numero positivo')
        
        
if __name__ == '__main__':
    unittest.main()