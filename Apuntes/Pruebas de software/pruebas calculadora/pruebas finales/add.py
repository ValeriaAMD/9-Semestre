from center.center import ope_central
from center.centerFlo import ope_central_flo
import unittest

class Testcalculadora(unittest.TestCase):

    def test_suma_v0_num_enteros(self):
        a = 22
        b = 11
        sum = a + b
        result = ope_central("0","0","22","11")
        self.assertEquals(sum,result)
    def test_suma_v1_num_enteros(self):
        a = 10
        b = 10
        sum = a + b
        result = ope_central("1","0","10","10")
        self.assertEquals(sum,result)
    def test_suma_v2_num_enteros(self):
        a = 20
        b = 20
        sum = a + b
        result = ope_central("2","0","20","20")
        self.assertEquals(sum,result)
    def test_suma_v3_num_enteros_negativos(self):
        a = -10
        b = 10
        sum = a + b
        result = ope_central("3","0","-10","10")
        self.assertEquals(sum,result)
    def test_suma_v4_num_enteros_negativos(self):
        a = 10
        b = -20
        sum = a + b
        result = ope_central("4","0","10","-20")
        self.assertEquals(sum,result)
    def test_suma_v5_num_enteros_negativos(self):
        a = -10
        b = -10
        sum = a + b
        result = ope_central("5","0","-10","-10")
        self.assertEquals(sum,result)
    def test_suma_v6_num_decimales(self):
        a = 22.2
        b = 11.1
        sum = a + b
        result = ope_central_flo("6","0","22.2","11.1")
        self.assertEquals(sum,result)
    def test_suma_v7_num_decimales_negativos(self):
        a = 15.3
        b = -15.3
        sum = a + b
        result = ope_central_flo("7","0","15.3","-15.3")
        self.assertEquals(sum,result)
    def test_suma_v8_num_decimales_negativos(self):
        a = -22.4
        b = 33.6
        sum = a + b
        result = ope_central_flo("8","0","-22.4","33.6")
        self.assertEquals(sum,result)
    def test_suma_v9_num_decimales_negativos(self):
        a = -50.5
        b = -50.5
        sum = a + b
        result = ope_central("9","0","-50.5","-50.5")
        self.assertEquals(sum,result)

if __name__ == '__main__':
    unittest.main()