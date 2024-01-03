import unittest
from Operaciones.division import division
class Test_division(unittest.TestCase):

    def test_div_enteros(self):
        n = 6
        r = 2
        resultado = division(n,r)
        self.assertEqual(resultado,3)
        
    def test_div_floats(self):
        n = 8.02
        r = 4
        resultado = division(n,r)
        self.assertEqual(resultado,2.005)

    def test_div_palabrainvalida(self):
        n = 'palabrota'
        r = 9
         
        with self.assertRaises(ValueError) as exc:
            division(n,r)
        
        self.assertEqual(str(exc.exception),'Base debe ser numerico')
    
    def test_divi_negativa(self):
        n = -9
        r = 3
         
        with self.assertRaises(ValueError) as exc:
            division(n,r)
        
        self.assertEqual(str(exc.exception),'ambos deben ser negativos o positivos')
        
    def test_div_negativos(self):
        n = 6
        r = -1
         
        with self.assertRaises(ValueError) as exc:
            division(n,r)
        
        self.assertEqual(str(exc.exception),'ambos deben ser negativos o positivos')
        
    def test_div_entre0(self):
        n = 6
        r = 0
         
        with self.assertRaises(ValueError) as exc:
            division(n,r)
        
        self.assertEqual(str(exc.exception),'no puede dividir entre 0')
        


if __name__ == '__main__':
    unittest.main()