import unittest
from operaciones.resta import resta
class Test_resta(unittest.TestCase):

    def test_resta_enteros(self):
        n = 5
        r = 2
        resultado = resta(n,r)
        self.assertEqual(resultado,3)
        
    def test_resta_floats(self):
        n = 9.03
        r = 4
        resultado = resta(n,r)
        self.assertEqual(resultado,5.03)

    def test_resta_palabrainvalida(self):
        n = 'otrap'
        r = 6
         
        with self.assertRaises(ValueError) as exc:
            resta(n,r)
        
        self.assertEqual(str(exc.exception),'Base debe ser numerico')
    
    def test_resta_negativa(self):
        n = -8
        r = 5
         
        with self.assertRaises(ValueError) as exc:
            resta(n,r)
        
        self.assertEqual(str(exc.exception),'ambos deben ser negativos o positivos')
        

        
    def test_resta_n_mayor_que_r(self):
        with self.assertRaises(ValueError) as exc:
            resta(7, 10)
        self.assertEqual(str(exc.exception), 'El valor de n no puede ser menor que n')


if __name__ == '__main__':
    unittest.main()