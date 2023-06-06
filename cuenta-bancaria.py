
#construyendo una cuenta bancaria, defino objeto

class Cuenta():
        #inicializo objeto
        def __init__(self, propietario, saldo, moneda):
            self.propietario = propietario
            self.saldo = saldo
            self.moneda = "pesos"

        #Invoco metodo get (leer propiedades de una clase que estan encapsuladas)

        def get_saldo(self):
              return self.saldo
        
        def get_propietario(self):
              return self.propietario
        
        def get_moenda(self):
              return self.moneda
        
        #Invoco metodo set (modificar propiedades de una clase por ejemplo pesos por dolares)

        def set_moneda(self, moneda):
              self.moneda = moneda

cuenta1 = Cuenta("Cecilia urrutia", 3000, "Peso Argentino")

print(cuenta1.get_saldo())
print(cuenta1.get_moneda())
cuenta1.set_moneda("Dolares")
print(cuenta1.get_moneda())
