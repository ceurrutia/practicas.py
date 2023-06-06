#defino la clase mascota

class Mascota():
    #inicializo constructor
    
    def __init__(self, nombre, edad, animal, propietario):
        #Atributos mascota
        self.nombre = nombre
        self.edad = edad
        self.animal = animal
        self.propietario = propietario
        
        

        #Creo el método string

        def __str__(self)-> str:
    
         return f'{self.nombre}, {self.edad}, {self.animal}, {self.propietario}'

#creo la lista
i = 0
lista = []

#Función sistema muestra los animales registrados
def sistema():
    k=0
    while k < len(lista):
        print(lista[k].nombre, "", lista[k].edad, "", lista[k].animal, "",lista[k].propietario,"" )
        k +=1
while i ==0:
    print("Menu - Seleccione la opción ")
    print("1. Registrar mascota: ")
    print("2. Consultar listado: ")
    print("3. Salir")
    opcion = int(input())
    if opcion == 1:
        print("Registrar mascota") 
       
        #inicio variables de entrada
       
        n = input("Ingrese nombre de la mascota: ")
        e = input("Ingrese la edad de la mascota: ")
        a = input("Ingrese el tipo de animal (Gato, perro, rana de felpa, hurón, loro): ")
        p = input("Ingrese el nombre del propietario del animalito: ")
        
       
        #Guardo los datos de entrada
       
        masc = Mascota(n, e, a, p)
        lista.append(masc)  
        
           
        print("Mascota registrada con éxito! ")
        print("Ha registrado a: ", n, "Edad: ",e, "Es de tipo: ",a , "Propietario: ",p )

    elif opcion == 2:
        print("Consulta de animales: ")
        sistema()
        
    elif opcion == 3:
        exit()
    else: 
        print("Opción inválida")




    
    
    
    
    
    