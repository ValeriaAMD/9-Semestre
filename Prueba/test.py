import unittest
from programas.opera import validar_numeros
class Test_Rectangulo_2(unittest.TestCase):
    
    def test_validar_numeros_enteros(self):
        n = 2
        r = 2
        resultado = validar_numeros(n,r)
        self.assertEquals(resultado,1)
        
    def test_resultado_rectangulo_floats(self):
        n = 1
        r = 3.1416
        resultado = validar_numeros(n,r)
        self.assertEquals(resultado,3.1416)

    def test_validar_numeros_n_invalida(self):
        n = 'Hola'
        r = 3
         
        with self.assertRaises(ValueError) as exc:
            validar_numeros(n,r)
        
        self.assertEqual(str(exc.exception),'debe ser numerico')
    
    def test_validar_numeros_altura_negativa(self):
        n = 2
        r = -2
         
        with self.assertRaises(ValueError) as exc:
            validar_numeros(n,r)
        
        self.assertEqual(str(exc.exception),'debe ser un numero positivo')
        

if __name__ == '__main__':
    unittest.main()