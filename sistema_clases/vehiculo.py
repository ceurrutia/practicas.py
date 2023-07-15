#defino objeto vehiculo

class Vehiculo:
    #inicializo clase
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    #defino metodo 
    def __str__(self ):
        return f'{self.color}, {self.ruedas}'
    
    class Coche:
        def __init__(self, velocidad, cilindrada):
            self.velocidad = velocidad
            self.cilindrada = cilindrada
            
    
            
       
            
        