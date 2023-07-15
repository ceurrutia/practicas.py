import datetime

#IMporta la fecha actual

fecha_actual= datetime.date.today()
print(fecha_actual)

#solicitamos al usuario que ingrese su dia de nacimiento

fecha_nac = input("Ingresa tu fecha de nacimiento: ")

try:
    fecha_nac = datetime.datetime.strptime(fecha_nac, "%d/%m/%Y").date()


#Lanzo una excepcion por si pone mal el formato
except ValueError:
    print("Formato de datos incorrecto. Asegurate de ingresar tus datos en el formato correcto dd/mm/aaaa")
    exit()
    
#Calculamos edad

edad = fecha_actual.year - fecha_nac.year
print(edad)
print("Tu edad actual es: ", edad, "anios")
#Verifico si cumplio anios en el anio o no

if (fecha_actual.year, fecha_actual.month, fecha_actual.day) < (fecha_nac.year, fecha_nac.month, fecha_nac.day):
    edad =+ 1
    
    
#Mostrar la edad actual y verifico si es mayo de 18
if edad >= 18:
        print("Eres mayor de edad")
else:
       print ("Eres joven, no es un sitio para ti")
    
