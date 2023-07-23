import datetime

'''De dos variables imprime el mayor'''

num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero : "))

if num1 > num2:
    print("El ", num1, "es mayor que ", num2)
elif num1 == num2 and num2 == num1:
    print("No se puede determnar el valor mayor")
else:
    print("El ", num2, "es mayor que ", num1)
    
'''De 3 variables ingresadas, imprime el numero mas alto de las tres'''

num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))
num3 = int(input("ingrese otro numero entero: "))

if num1 > num2 and num1 > num3:
    print("El numero mayor es ", num1)
elif num1 ==0 and num2 ==0 and num3 ==0:
    print("Introduzca un numero que no sea 0")

elif num2 > num1 and num2 > num3:
    print(("El numero mas alto es: ", num2))
elif num3 > num1 and num3 > num2:
    print("El numero mayor es ", num3)
elif num1 == num2 and num2 == num3:
    print("No se puede efectuar la comprobacion ya que los tres numeros son iguales")
else:
    print("No se puede establecer el numero mayor ")   

'''Preguntar la edad a un usuario y establecr si es mayor de edad'''

fecha_actual= datetime.date.today()
print(fecha_actual)

fecha_nac = input("Ingrese su fecha de nac: ")
fecha_nac = datetime.datetime.strptime(fecha_nac, "%d/%m/%Y").date()

#Establecemos edad actual

Edad = fecha_actual.year - fecha_nac.year
print("Usted tiene: " , Edad, "anios")

#Comprobamos si es mayor de 18

if Edad >=18:
    print("Usted es mayor de edad")
else:
    print("Juira a dormir a casa con su mama ")
    
