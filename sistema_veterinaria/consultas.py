
#Objeto consultas

class Consultas:
    #inicio constructor
    def __init__(self, motivo_consulta, fecha, id_animal):

    #atributos consultas
        self.nombre = id_animal
        self.tipo_consulta = motivo_consulta
        self.fecha = fecha
        

        #initio metodo string

        def __str__(self):
            return f'{self.id_animal} + {self.motivo_consulta} + {self.fecha} '
        
        #metodos mostrar con GET
        
            


         