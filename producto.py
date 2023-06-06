'''Crear el class producto, que me muestre sus atributos, poder modificar los valores'''


#defino objeto producto 

class Producto():
    #Inicializo clase
    def __init__(self, descripcion, cantidad, precio):
        super().__init__() #Super es la superclase
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    #Creo el método string

    def __str__(self)-> str:
        return f'{self.descripcion}, {self.cantidad}, {self.precio}'
    
    #Creo metodo get

    def __getattribute__(self, name: str) -> str:
        if name == "precio":
            p = super(). __getattribute__(name)
            p = p-5
            return str(p)
        return str(super(). __getattribute__(name))
    
    #Creo metodo set

    def __setattr__(self, name: str, value) -> None:
        if name == "cantidad":
            if type(value) is not int:
                raise ValueError("Tipo de dato incorrecto")
        elif name == "precio":
                if type(value) is not float:
                    raise ValueError("Tipo de dato incorrecto")
        return super(). __setattr__(name, value)
            
    def __getattr__(self, name: str) -> str:
        return name + " no es válido."
    
    #Creo los productos
    
prod1 = Producto("Computadora", 12, 100.35)

    # Invoco get atribute
print(prod1)

prod1.cantidad = 10
prod1.precio = 90.55
prod1.descripcion = "Dell 8760"

print(prod1)