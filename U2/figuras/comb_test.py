import unittest
from areas.combinacion import calcular_combi 

class TestCalcularCombi(unittest.TestCase):

    def test_calcular_combi_enteros(self):
        z = 5
        r = 3
        resultado = calcular_combi(z, r)
        self.assertEqual(resultado, 10)

    def test_calcular_combi_valores_negativos(self):
        with self.assertRaises(ValueError) as exc:
            calcular_combi(-2, 3)
        self.assertEqual(str(exc.exception), 'Ambos valores deben ser positivos')

    def test_calcular_combi_r_mayor_que_z(self):
        with self.assertRaises(ValueError) as exc:
            calcular_combi(3, 5)
        self.assertEqual(str(exc.exception), 'El valor de r no puede ser mayor que z')

    def test_calcular_combi_no_enteros(self):
        with self.assertRaises(ValueError) as exc:
            calcular_combi(2, 'Hola')
        self.assertEqual(str(exc.exception), 'Ambos valores deben ser enteros')

if __name__ == '__main__':
    unittest.main()