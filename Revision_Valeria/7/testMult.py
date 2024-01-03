import unittest
from operaciones.multiplicacion import multiplicacion
class Test_mu(unittest.TestCase):

    def test_mu_enteros(self):
        n = 6
        r = 2
        resultado = multiplicacion(n,r)
        self.assertEqual(resultado,12)
        
    def test_mu_floats(self):
        n = 10.1
        r = 4
        resultado = multiplicacion(n,r)
        self.assertEqual(resultado,40.4)

    def test_mu_palabrainvalida(self):
        n = 'palabr'
        r = 3
         
        with self.assertRaises(ValueError) as exc:
            multiplicacion(n,r)
        
        self.assertEqual(str(exc.exception),'Base debe ser numerico')
    
    def test_mu_negativa(self):
        n = -9
        r = 3
         
        with self.assertRaises(ValueError) as exc:
            multiplicacion(n,r)
        
        self.assertEqual(str(exc.exception),'ambos deben ser negativos o positivos')
        
  
if __name__ == '__main__':
    unittest.main()