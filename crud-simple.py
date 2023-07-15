#crear un crud simple del objeto Persona, que permita modificar, listar y eliminar registro


class Persona:
  #inicializo clase
  def __init__(self, nombre, edad, mail):
    self.nombre = nombre
    self.edad = edad
    self.mail = mail


#self es el identificador

personas = []


def agregar_persona(nombre, edad, mail):
  persona = Persona(nombre, edad, mail)
  personas.append(persona)


def eliminar_persona(nombre):
  for persona in personas:
    if persona.nombre == nombre:
      personas.remove(persona)


def modificar_persona(nombre, new_nombre, new_edad, new_mail):
  for persona in personas:
    if persona.nombre == nombre:
      persona.nombre = new_nombre
      persona.edad = new_edad
      persona.mail = new_mail


def imprimir_personas():
  for persona in personas:
    print("Nombre: ", persona.nombre)
    print("Edad: ", persona.edad)
    print("Mail: ", persona.mail)
    print("---------")


agregar_persona("Juan", 30, "juan@test.com")
agregar_persona("Rocio", 26, "rdecire@test.com")
agregar_persona("Clemente", 22, "clem@test.com")

imprimir_personas()

modificar_persona("Juan", "Juan Carlos", 38, "juancar@mail.com")
modificar_persona("Rocio", "Manuela Rocio", 26, "roco@mail.com")

imprimir_personas()

#Probar eliminar descomentando el eliminar

eliminar_persona("Clemente")
imprimir_personas()