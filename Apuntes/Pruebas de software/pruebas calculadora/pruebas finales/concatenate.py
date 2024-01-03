from center.centerCo import ope_central_concatenación
import unittest

class Testcalculadora(unittest.TestCase):

    def test_conca_v0_num_enteros(self):
        a = 22
        b = 11
        concat = str(a) + str(b)
        result = ope_central_concatenación("0", "4","22","11")
        self.assertEquals(concat, result)
    def test_conca_v1_num_enteros(self):
        a = 10
        b = 10
        co = str(a) + str(b)
        result = ope_central_concatenación("1","4","10","10")
        self.assertEquals(co,result)
    def test_conca_v2_num_enteros(self):
        a = 20
        b = 20
        co = str(a) + str(b)
        result = ope_central_concatenación("2","4","20","20")
        self.assertEquals(co,result)
    def test_conca_v3_num_enteros_negativos(self):
        a = -10
        b = 10
        co = str(a) + str(b)
        result = ope_central_concatenación("3","4","-10","10")
        self.assertEquals(co,result)
        
    def test_conca_v4_num_enteros_negativos(self):
        a = 10
        b = -20
        co = str(a) + str(b)
        result = ope_central_concatenación("4","4","10","-20")
        self.assertEquals(co,result)
        
    def test_conca_v5_num_enteros_negativos(self):
        a = -10
        b = -10
        co = str(a) + str(b)
        result = ope_central_concatenación("5","4","-10","-10")
        self.assertEquals(co,result)
        
    def test_conca_v6_num_decimales(self):
        a = 22.2
        b = 11.1
        co = str(a) + str(b)
        result = ope_central_concatenación("6","4","22.2","11.1")
        self.assertEquals(co,result)
        
    def test_conca_v7_num_decimales_negativos(self):
        a = 15.3
        b = -15.3
        co = str(a) + str(b)
        result = ope_central_concatenación("7","4","15.3","-15.3")
        self.assertEquals(co,result)
        
    def test_conca_v8_num_decimales_negativos(self):
        a = -22.4
        b = 33.6
        co = str(a) + str(b)
        result = ope_central_concatenación("8","4","-22.4","33.6")
        self.assertEquals(co,result) 
        
    def test_conca_v9_num_decimales_negativos(self):
        a = -50.5
        b = -50.5
        co = str(a) + str(b)
        result = ope_central_concatenación("9","4","-50.5","-50.5")
        self.assertEquals(co,result)

if __name__ == '__main__':
    unittest.main()