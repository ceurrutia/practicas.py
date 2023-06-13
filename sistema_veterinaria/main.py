from mascotas import Mascota

#programa principal
#creo la lista
i = 0
lista = []

agrega_mascota = True

#Función sistema muestra los animales registrados
def sistema():
  lista_mascotas = 0
  while lista_mascotas < len(lista):
    print( lista[lista_mascotas].id, '', lista[lista_mascotas].nombre, " ", lista[lista_mascotas].edad, " ", lista[lista_mascotas].animal, " ",
          lista[lista_mascotas].raza, " ", lista[lista_mascotas].color, " ", lista[lista_mascotas].tamanio, " ", lista[lista_mascotas].motivo_consulta, " ", lista[lista_mascotas].nombre_duenio, " ", lista[lista_mascotas].telefono_duenio)
    lista_mascotas += 1
    
    
def eliminar_mascota(masc):
    orden = int(input("Ingrese el id de la mascota que desea eliminar: "))
    #se recorre la lista, si encuentra un objeto con id igual al ingresado lo elimina
    for i in range(1, len(lista)):
        if lista[i].id == int(orden):
            lista.remove(masc)
    print("Mascota eliminada de la lista")


while i == 0:
  print("Menu - Seleccione la opción ")
  print("1. Registrar mascota: ")
  print("2. Agregar una nueva mascota: ")
  print("3. Consultar listado: ")
  print("4: Eliminar mascota por ID:")
  print("5. Salir")
  opcion = int(input())

  if opcion == 1:
    print("Registrar mascota")

    #inicio variables de entrada

    nom = input("Ingrese nombre de la mascota: ")
    ed = input("Ingrese la edad de la mascota: ")
    ani = input(
      "Ingrese el tipo de animal (Gato, perro, rana de felpa, hurón, loro): ")
    raz = input("Ingrese la raza: ")
    col= input("Ingrese color: ")
    tam = input("Ingrese tamaño: ")
    mot_cons = input("Motivo de la consulta: ")
    nom_duenio = input("Ingrese nombre del dueño: ")
    tel_duenio = input("Ingrese teléfono del dueño: ")
  
    #Guardo los datos de entrada

    masc = Mascota(id, nom, ed, ani, raz, col, tam, mot_cons, nom_duenio, tel_duenio)
    lista.append(masc)

    print("Mascota registrada con éxito! ")
    print("Legajo:", Mascota.id)
    print("Ha registrado a: ", nom, " Edad: ", ed, "Es de tipo: ", ani,
          "Raza: ", raz, "Es de color: ", col, "Tamaño: ", tam, "El motivo de la consulta es: " , mot_cons, "Su dueño es: ", nom_duenio, "Su teléfono es: ", tel_duenio)

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
        print("Eliminar mascota:")
        eliminar_mascota(masc)
        print()
     
  elif opcion == 5:
        print("Has salido con éxito. Adiós")
        exit()
  else:
    print("Opción inválida")
