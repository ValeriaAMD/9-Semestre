import unittest
from operaciones.division import division
class Test_division(unittest.TestCase):

    def test_div_enteros(self):
        n = 6
        r = 16
        resultado = division(n,r)
        self.assertEqual(resultado,0.37)
        
    def test_div_floats(self):
        n = 16.48
        r = 3
        resultado = division(n,r)
        self.assertEqual(resultado,5.49)

    def test_div_palabrainvalida(self):
        n = 'palabrota'
        r = 9
         
        with self.assertRaises(ValueError) as exc:
            division(n,r)
        
        self.assertEqual(str(exc.exception),'Base debe ser numerico')
    
        
    def test_div_entre0(self):
        n = 6
        r = 0
         
        with self.assertRaises(ValueError) as exc:
            division(n,r)
        
        self.assertEqual(str(exc.exception),'no puede dividir entre 0')
        


if __name__ == '__main__':
    unittest.main()