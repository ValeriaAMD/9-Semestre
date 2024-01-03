import unittest
from operaciones.suma import suma
class Test_suma(unittest.TestCase):

    def test_suma_enteros(self):
        n = 9
        r = 1
        resultado = suma(n,r)
        self.assertEqual(resultado,10)
        
    def test_suma_floats(self):
        n = 7.09
        r = 2
        resultado = suma(n,r)
        self.assertEqual(resultado,9.09)

    def test_suma_palabrainvalida(self):
        n = 'palabrA'
        r = 7
         
        with self.assertRaises(ValueError) as exc:
            suma(n,r)
        
        self.assertEqual(str(exc.exception),'Base debe ser numerico')
    
    def test_suma_negativa(self):
        n = 5
        r = -2
         
        with self.assertRaises(ValueError) as exc:
            suma(n,r)
        
        self.assertEqual(str(exc.exception),'ambos deben ser negativos o positivos')
        
    def test_suma_negativos(self):
        n = -9
        r = 2
         
        with self.assertRaises(ValueError) as exc:
            suma(n,r)
        
        self.assertEqual(str(exc.exception),'ambos deben ser negativos o positivos')


if __name__ == '__main__':
    unittest.main()