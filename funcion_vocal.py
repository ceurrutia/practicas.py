'''
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
'''

Buscarvocal = input("Ingresa una vocal: ")

if Buscarvocal == "a" or Buscarvocal == "e" or Buscarvocal =="i" or Buscarvocal =="o" or Buscarvocal == "u":
    print (Buscarvocal,  "Es una vocal")
elif Buscarvocal == "A" or Buscarvocal == "E" or Buscarvocal =="I" or Buscarvocal =="O" or Buscarvocal == "U":
    print (Buscarvocal,  "Es una vocal")
else: 
    print("No es una vocal")




def EsVocal(x) : 
    #defino condicionales
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x== "O" or x == "U":
        return True
    else:
        return False


'''
Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena 
"odnaborp yotse"
'''

def inversa(cadena):
    invertida = ''
    cont = len(cadena)
    indice = -1
    while cont >=1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida