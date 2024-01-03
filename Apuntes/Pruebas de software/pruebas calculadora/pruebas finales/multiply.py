from center.center import ope_central
from center.centerFlo import ope_central_flo
import unittest

class Testcalculadora(unittest.TestCase):

    def test_multiplicacion_v0_num_enteros(self):
        a = 7
        b = 5
        multiplicacion = a * b
        result = ope_central("0","2","7","5")
        self.assertEquals(multiplicacion,result)
    def test_multiplicacion_v1_num_enteros(self):
        a = 6
        b = 7
        multiplicacion = a * b
        result = ope_central("1","2","6","7")
        self.assertEquals(multiplicacion,result)
    def test_multiplicacion_v2_num_enteros(self):
        a = 7
        b = 7
        multiplicacion = a * b
        result = ope_central("2","2","7","7")
        self.assertEquals(multiplicacion,result)
    def test_multiplicacion_v3_num_ent_negat(self):
        a = -7
        b = 4
        multiplicacion = a * b
        result = ope_central("3","2","-7","4")
        self.assertEquals(multiplicacion,result)
    def test_multiplicacion_v4_num_ent_negativos(self):
        a = 8
        b = -9
        multiplicacion = a * b
        result = ope_central("4","2","8","-9")
        self.assertEquals(multiplicacion,result)
    def test_multiplicacion_v5_num_enteros_negativos(self):
        a = -11
        b = -11
        multiplicacion = a * b
        result = ope_central("5","2","-11","-11")
        self.assertEquals(multiplicacion,result)
    def test_multiplicacion_v6_num_decimales(self):
        a = 42.2
        b = 51.1
        multiplicacion = a * b
        result = ope_central_flo("6","2","42.2","51.1")
        self.assertEquals(multiplicacion,result)
    def test_multiplicacion_v7_num_decimales_negat(self):
        a = 20.1
        b = -35.5
        multiplicacion = a * b
        result = ope_central("7","2","20.1","-35.5")
        self.assertEquals(multiplicacion,result)
    def test_multiplicacion_v8_num_decimal_negat(self):
        a = -22.4
        b = 33.6
        multiplicacion = a * b
        result = ope_central_flo("8","2","-22.4","33.6")
        self.assertEquals(multiplicacion,result)
    def test_multiplicacion_v9_num_decimal_neg(self):
        a = 33.3
        b = 66.6
        multiplicacion = a * b
        result = ope_central("9","2","33.3","66.6")
        self.assertEquals(multiplicacion,result)

if __name__ == '__main__':
    unittest.main()