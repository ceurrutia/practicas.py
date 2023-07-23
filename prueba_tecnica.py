'''Usando metodos mas comunes'''


'''
SPLIT De forma predeterminada, divide la cadena en espacios.
Podemos proporcionar el delimitador como argumento 
para el método.
''' 

a = "This is Esparta"
a.split()
['This', 'is', 'Esparta']
a = "1, 2, 3, 4, 5, 6"
a.split(", ")
['1', '2', '3', '4', '5', '6']
        
        
HolaM = "Hola mundo"
print(HolaM)

nombre = input("Inredouzca su nombre: ")
print("hola, ", nombre)

'''Escribe un programa que pregunte al usuario por el número de horas 
trabajadas y el costo por hora. Después debe mostrar por 
pantalla el pago que le corresponde.'''

horas = float(input("Introduce tus horas trabajadas: "))
coste_horas = float(input ("Introduce cuanto cobras por hora: "))
pago = horas * coste_horas
print("Tu paga es: ",pago)

'''
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años,
y muestre por pantalla el capital obtenido en la inversión.
'''
cant_invertir = float(input("Ingrese la cantidad a invertir: "))
int_anual = float(input("Cual es el interes anual?: "))
num_anios = int(input("Introduzca la cantidad de anios: "))

print("El capital final sera: ", str(round(cant_invertir * (int_anual / 100 + 1) ** num_anios, 2)))