#defino la clase mascota

class Mascota():
    #inicializo constructor
    
    def __init__(self, nombre, especie, animal, raza, nombre_duenio):
        #Atributos mascota
        self.nombre = nombre
        self.especie = especie
        self.animal = animal
        self.raza = raza
        self.nombre_duenio = nombre_duenio

        #Creo el método string

        def __str__(self)-> str:
    
         return f'{self.nombre}, {self.especie}, {self.animal}, {self.raza}, {self.nombre_duenio}'

#creo la lista
i = 0
lista = []

#Función sistema muestra los animales registrados
def sistema():
    k=0
    while k < len(lista):
        print(lista[k].nombre, "", lista[k].especie, "", lista[k].animal, "",lista[k].raza, "", lista([k].nombre_duenio))
        k+=1

while i ==0:
    print("Menu - Seleccione la opción ")
    print("1. Registrar mascota: ")
    print("2. Consultar listado: ")
    print("3. Salir")
    opcion = int(input())
    if opcion==1:
        print("Registrar mascota") 
       
        #inicio variables de entrada
       
        n = input("Ingrese nombre de la mascota: ")
        e = input("Ingrese la especie de la mascota: (Canino, felino, ave, mustélido, etc): ")
        a = input("Ingrese el tipo de animal (Gato, perro, rana de felpa, hurón, loro): ")
        r = input("Ingrese la raza del animalito: ")
        d = input("Ingrese nombre del dueño de la mascota: ")
       
        #Guardo los datos de entrada
       
        masc = Mascota(n, e, a, r, d)
        lista.append(masc)
        
        
        print("Mascota registrada con éxito! ")
        print("Ha registrado a: ", n, "Especie: ",e, "Es de tipo: ",a , "Raza: ",r, "Su dueño/a es: ",d )

    elif opcion == 2:
        print("Consulta listado ")
        
    elif opcion == 3:
        exit()
    else: 
        print("Opción inválida")




    
    
    
    
    
    