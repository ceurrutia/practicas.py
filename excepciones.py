#La excepcion ocurre cuando el sistema me indica un error, 
# ejemplo: un indice fuera de rengo, 
# el lenguaje no puede hacer nada, la excepcion detiene el prgrama

#error type
#print(2- '1')

#No se puede restar un entero con un string

#si se manejar la excepcion puedo controlar mi programa
try: #capturo el bloque que puede tener un error y manejea la excepcion
    
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    resultado = num1 / num2 #No se divide por 0, da error: division by zero
    print(resultado)
    
except ValueError:
    print("Debe ingresar valores numéricos.")
except ZeroDivisionError:
    print("El denominador no puede ser 0.")   
except:
    print("Ha ocurrido un error.")
    
else:
    print(resultado)
finally:
    print("Fin del bloque try-except")

print("Fin del programa")
#Los except funicona como switch, entra a un bucle,
#El except protege de que no se te cuelgue el sistema

# la estructura siempre es try - except - finally
'''Finally se puede usar para contar cantidad de registros.
Para cerrar archivos de texto, 
Para garantizar que las lineas se ejecuten despues de haber 
tenido un error, haya habido o no'''

'''
f = open('archivo.txt')
s = f.readline()
i = int(s.rstrip('\n'))
f.close()
'''

#Generar nosotros una excepcion

class NumeroNegativoError(Exception):
    pass

#usando raise, se relanza la funcion

num = int(input("Ingrese un numero: "))
if num < 0:
    raise NumeroNegativoError('El numero debe ser positivo o cero.')
print(num)


#La excepcion ocurre y se propaga al resto de los metodos

#Assert tiene su propia except es una afirmacion que no se dio
#queda asociada a un mensaje.











