'''Crear la clase Persona con los métodos “set_nombre”, “set_edad”,
“get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo
Persona e imprimirlos por consola.'''

#defino clase persona
from typing import Any


class Persona():
    #Inicializo clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
Cecilia = Persona('Cecilia', '51')
print(Cecilia)

    



        