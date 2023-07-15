#test de pruebas

from lambdas import ponerPrefijo
#importo metodo pata testar


import unittest

class TestBasica(unittest.TestCase):
    def test_es_mayor_que(self):
        self.assertTrue(200 > 30) #Le especifico una asercion booleanda
        
if __name__ == "__main__":
    unittest.main()  #Resultado ok
    
#Otro case

class test_saludar(unittest.TestCase):
        def nombre_Tito(self):
            self.assertTrue(ponerPrefijo == "Sr.")
            
if ponerPrefijo == "Sr.":
    unittest.main()
     