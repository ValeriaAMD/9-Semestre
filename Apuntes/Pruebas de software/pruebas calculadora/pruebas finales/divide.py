from center.center import ope_central
import unittest

class Testcalculadora(unittest.TestCase):

    def test_divi_v0_num_enteros(self):
        a = 30
        b = 5
        divi = a / b
        result = ope_central("0","3","30","5")
        self.assertEquals(divi,result)
    def test_divi_v1_num_enteros(self):
        a = 11
        b = 11
        divi = a / b
        result = ope_central("1","3","11","11")
        self.assertEquals(divi,result)
    def test_divi_v2_num_enteros(self):
        a = 100
        b = 100
        divi = a / b
        result = ope_central("2","3","100","100")
        self.assertEquals(divi,result)
    def test_divi_v3_num_ent_negat(self):
        a = -30
        b = 10
        divi = a / b
        result = ope_central("3","3","-30","10")
        self.assertEquals(divi,result)
    def test_divi_v4_num_ent_negativos(self):
        a = 11
        b = -21
        divi = a / b
        result = ope_central("4","3","11","-21")
        self.assertEquals(divi,result)
    def test_divi_v5_num_enteros_negativos(self):
        a = -11
        b = -11
        divi = a / b
        result = ope_central("5","3","-11","-11")
        self.assertEquals(divi,result)
    def test_divi_v6_num_decimales(self):
        a = 22.2
        b = 11.1
        divi = a / b
        result = ope_central("6","3","22.2","11.1")
        self.assertEquals(divi,result)
    def test_divi_v7_num_decimales_negat(self):
        a = 20.1
        b = -35.5
        divi = a / b
        result = ope_central("7","3","20.1","-35.5")
        self.assertEquals(divi,result)
    def test_divi_v8_num_decimal_negat(self):
        a = -22.4
        b = 33.6
        divi = a / b
        result = ope_central("8","3","-22.4","33.6")
        self.assertEquals(divi,result)
    def test_divi_v9_num_decimal_neg(self):
        a = -51.5
        b = -51.5
        divi = a / b
        result = ope_central("9","3","-51.5","-51.5")
        self.assertEquals(divi,result)

if __name__ == '__main__':
    unittest.main()