import unittest
from programas.combinacion import combinacion
def test_area_rectangulo_altura_negativa(self):
        n = 2
        r = -2
         
        with self.assertRaises(ValueError) as exc:
            combinacion(n,r)
        
        self.assertEqual(str(exc.exception),'Altura debe ser un numero positivo')