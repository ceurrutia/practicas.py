
#Clases sistema bancario

class sistema_banco(object):
    #inicializo constructor
    def __init__(self, id, monto_depositado, monto_extraer, saldo):
        #atributos
        self.id_user = id
        self.monto_depositado = monto_depositado
        self.monto_extraer = monto_extraer
        self.saldo = saldo
        
        #Metodo
        def __str__(self):
            return f'{self.id},{self.monto_depositado}, {self.monto_extraer}, {self.saldo}'

class usuario (object):
    #inicializo contructor
	def __init__(self, dni, clave):
		self.dni = dni
		self.clave = clave
		
Usuario1 = usuario (22225977, 'Kaigaku')

print (Usuario1.dni, Usuario1.clave)