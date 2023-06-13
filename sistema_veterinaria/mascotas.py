#defino la clase mascota
class Mascota():
  id = 0
  
  #inicializo constructor
  def __init__(self, id, nombre, edad, animal, raza, color, tamanio, motivo_consulta, nombre_duenio, telefono_duenio):
    #Atributos mascota
    Mascota.id += 1
    self.id = Mascota.id
    self.nombre = nombre
    self.edad = edad
    self.animal = animal
    self.raza = raza
    self.color = color
    self.tamanio = tamanio
    self.motivo_consulta = motivo_consulta
    self.nombre_duenio = nombre_duenio
    self.telefono_duenio = telefono_duenio


    #Creo el método string

    def __str__(self) -> str:

      return f'ID:{self.id},{self.nombre}, {self.edad}, {self.animal}, {self.raza}, {self.color}, {self.tamanio}, {self.motivo_consulta} ,{self.nombre_duenio}, {self.telefono_duenio}'







    
    
    
    
    
    