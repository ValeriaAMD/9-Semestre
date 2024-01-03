import unittest
from programas.factorial import factorial
class Test_factorial_2(unittest.TestCase):
    

    def test_factorial(self):
        n = 3
        area = factorial(n)
        self.assertEquals(area,6)
        
    def test_factorial_floats(self):
        r = 3.1416

        with self.assertRaises(ValueError) as exc:
          factorial(r)
        self.assertEqual(str(exc.exception),'no admite decimales')

    def test_factorial_n_invalida(self):
        n = 'Hola'
         
        with self.assertRaises(ValueError) as exc:
            factorial(n)
        
        self.assertEqual(str(exc.exception),'debe ser numerico')
    
    def test_factorial_negativa(self):
        r = -2
         
        with self.assertRaises(ValueError) as exc:
            factorial(r)
        
        self.assertEqual(str(exc.exception),'debe ser un numero positivo')
        
        
if __name__ == '__main__':
    unittest.main()