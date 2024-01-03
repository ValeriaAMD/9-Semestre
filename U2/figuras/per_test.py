import unittest
from areas.permutacion import calcular_perm  
class TestCalcularPerm(unittest.TestCase):

    def test_calcular_perm_enteros(self):
        n = 5
        r = 3
        resultado = calcular_perm(n, r)
        self.assertEqual(resultado, 60)

    def test_calcular_perm_valores_negativos(self):
        with self.assertRaises(ValueError) as exc:
            calcular_perm(-2, 3)
        self.assertEqual(str(exc.exception), 'Ambos valores deben ser positivos')

    def test_calcular_perm_r_mayor_que_n(self):
        with self.assertRaises(ValueError) as exc:
            calcular_perm(3, 5)
        self.assertEqual(str(exc.exception), 'El valor de r no puede ser mayor que n')

    def test_calcular_perm_no_enteros(self):
        with self.assertRaises(ValueError) as exc:
            calcular_perm(2, 'Hola')
        self.assertEqual(str(exc.exception), 'Ambos valores deben ser enteros')

if __name__ == '__main__':
    unittest.main()
