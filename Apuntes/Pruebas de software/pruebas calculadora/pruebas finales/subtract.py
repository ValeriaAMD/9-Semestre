from center.center import ope_central
from center.centerFlo import ope_central_flo
import unittest

class Testcalculadora(unittest.TestCase):

    def test_resta_v0_num_enteros(self):
        a = 30
        b = 5
        resta = a - b
        result = ope_central("0","1","30","5")
        self.assertEquals(resta,result)
    def test_resta_v1_num_enteros(self):
        a = 11
        b = 11
        resta = a - b
        result = ope_central("1","1","11","11")
        self.assertEquals(resta,result)
    def test_resta_v2_num_enteros(self):
        a = 100
        b = 100
        resta = a - b
        result = ope_central("2","1","100","100")
        self.assertEquals(resta,result)
    def test_resta_v3_num_ent_negat(self):
        a = -30
        b = 10
        resta = a - b
        result = ope_central("3","1","-30","10")
        self.assertEquals(resta,result)
    def test_resta_v4_num_ent_negativos(self):
        a = 11
        b = -21
        resta = a - b
        result = ope_central("4","1","11","-21")
        self.assertEquals(resta,result)
    def test_resta_v5_num_enteros_negativos(self):
        a = -11
        b = -11
        resta = a - b
        result = ope_central("5","1","-11","-11")
        self.assertEquals(resta,result)
    def test_resta_v6_num_decimales(self):
        a = 22.2
        b = 11.1
        resta = a - b
        result = ope_central_flo("6","1","22.2","11.1")
        self.assertEquals(resta,result)
    def test_resta_v7_num_decimales_negat(self):
        a = 20.1
        b = -35.5
        resta = a - b
        result = ope_central_flo("7","1","20.1","-35.5")
        self.assertEquals(resta,result)
    def test_resta_v8_num_decimal_negat(self):
        a = -22.4
        b = 33.6
        resta = a - b
        result = ope_central("8","1","-22.4","33.6")
        self.assertEquals(resta,result)
    def test_resta_v9_num_decimal_neg(self):
        a = -51.5
        b = -51.5
        resta = a - b
        result = ope_central("9","1","-51.5","-51.5")
        self.assertEquals(resta,result)

if __name__ == '__main__':
    unittest.main()