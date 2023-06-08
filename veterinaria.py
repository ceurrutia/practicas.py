#defino la clase mascota
class Mascota():
  id = 0
  
  #inicializo constructor
  
  def __init__(self, id, nombre, edad, animal, propietario, telefono):
    #Atributos mascota
    Mascota.id += 1
    self.id = Mascota.id
    self.nombre = nombre
    self.edad = edad
    self.animal = animal
    self.propietario = propietario
    self.telefono = telefono
    
    

    #Creo el método string

    def __str__(self) -> str:
      return f' ID:{self.id}, {self.nombre}, {self.edad}, {self.animal}, {self.propietario}, {self.telefono}'

#creo la lista
i = 0
lista = []

agrega_mascota = True

#Función sistema muestra los animales registrados
def sistema():
  k = 0
  while k < len(lista):
    print(lista[k].id," ", lista[k].nombre, " ", lista[k].edad, " ", lista[k].animal, " ",
          lista[k].propietario, " ", lista[k].telefono)
    k += 1


while i == 0:
  print("Menu - Seleccione la opción ")
  print("1. Registrar mascota: ")
  print("2. Agregar una nueva mascota: ")
  print("3. Consultar listado: ")
  print("4. Salir")
  opcion = int(input())
  if opcion == 1:
    print("Registrar mascota")

    #inicio variables de entrada
    
    nom = input("Ingrese nombre de la mascota: ")
    ed = input("Ingrese la edad de la mascota: ")
    ani = input("Ingrese el tipo de animal (Gato, perro, rana de felpa, hurón, loro): ")
    prop = input("Ingrese el nombre del propietario del animalito: ")
    tel = input("Ingrese su teléfono de contacto: ")

    #Guardo los datos de entrada

    masc = Mascota(id, nom, ed, ani, prop, tel)
    lista.append(masc)

    print("Mascota registrada con éxito! ")
    print("Legajo:", Mascota.id)
    print("Ha registrado a:", nom, "Edad: ", ed, "Es de tipo: ",ani,
          "Propietario: ",prop, "Teléfono de contacto: ",tel)

  elif opcion == 2:
    opcion = input("¿Quieres agregar una nueva mascota?(si/no): ").lower()
   #Valido que escriba solo si o no
    while opcion != "si" and opcion != "no":
      print("Opción no disponible, intentalo de nuevo.")
      break
    if opcion == "si":
      print("Agregala ingresando el numero 1")
    elif opcion == "no":
      print("Has salido con éxito. Adiós")
      exit()

  elif opcion == 3:
    print("Consulta de animales ingresados en el sistema: ")
    sistema()  #Trae la lista 
  elif opcion == 4:
        print("Has salido con éxito. Adiós")
        exit()
  else:
    print("Opción inválida")