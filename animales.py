#defino la clase animal

class Animal:
    #atributos
    def __init__(self, id, nombre, tipo, edad, color, peso, telefono):
       #constructor
       self.id = 0
       self.nombre = nombre
       self.tipo = tipo
       self.edad = edad
       self.color = color
       self.peso = peso
       self.telefono = telefono
       
       #creo metodo string
       
    def __str__(self):
     return f'{self.id} {self.nombre} {self.tipo} {self.edad} {self.color} {self.peso} {self.telefono}'
           
animales = [] 

#pido ingreso de datos

nombre = input("Ingrese el nombre:")  
tipo = input("Ingrese tipo de animal:") 
edad = (input("Ingrese la edad:"))
color = input("Ingrese el color:")
peso =(input("Ingrese peso: "))
telefono = input("Ingrese telefono: ")

#Creo instancias para agregar a una lista

animales.append(Animal(1, "sumi", "gato", 12, "marron", 5, 1167280345))
animales.append(Animal(2, "Atun", "gato", 4, "blanca", 5, 11672890))  

#recorro con for
for animal in animales:
    print(animal.id, animal.nombre, animal.tipo, animal.edad, animal.peso, animal.telefono)