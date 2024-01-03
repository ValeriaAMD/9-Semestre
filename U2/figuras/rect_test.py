import unittest
from areas.rectangulo import area_rectangulo
class Test_Rectangulo_2(unittest.TestCase):

    def test_area_rectangulo_enteros(self):
        base = 2
        altura = 4
        area = area_rectangulo(base,altura)
        self.assertEquals(area,8)
        
    def test_area_rectangulo_floats(self):
        base = 1
        altura = 3.1416
        area = area_rectangulo(base,altura)
        self.assertEquals(area,3.1416)

    def test_area_rectangulo_base_invalida(self):
        base = 'Hola'
        altura = 3
         
        with self.assertRaises(ValueError) as exc:
            area_rectangulo(base,altura)
        
        self.assertEqual(str(exc.exception),'Base debe ser numerico')
    
    def test_area_rectangulo_altura_negativa(self):
        base = 2
        altura = -2
         
        with self.assertRaises(ValueError) as exc:
            area_rectangulo(base,altura)
        
        self.assertEqual(str(exc.exception),'Altura debe ser un numero positivo')


if __name__ == '__main__':
    unittest.main()