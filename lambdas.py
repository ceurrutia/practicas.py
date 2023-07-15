#lambda funciones anonimas,manera compacta de escribir una función si solo necesitas una expresión corta

#definir funcion lambda
suma = lambda a, b: a + b
print(suma(5 , 5))
print(suma(3 , 3))
    
saludar = lambda nombre: print(f'Hola {nombre}')
saludar('Pepe')
saludar('Tito')

maximo = lambda a,b,c: f'El maximo entre {a}, {b}, {c} es {max(a,b,c)}'
print(maximo(3,4,5))
print(maximo(10, 99,-50))

#curiosidad chula: las podemos usar dentro de funciones convencionales

#prefijos para nombres

def ponerPrefijo(prefijo):
    return lambda nombre:  f'{prefijo} {nombre}'
#nobre es el argumento

addMr = ponerPrefijo("Mr.")
addSr = ponerPrefijo ("Sr.")
addMiss = ponerPrefijo("Miss.")

print(addMr("Carlos"))
print(addSr("Pedro"))
print(addMiss("Nerea"))

def elevarA(exponente):
    return lambda base: base** exponente

def elevarB(exponente):
    return lambda base: base ** exponente

elevarCuadrado = elevarA(2)
elevarCubo = elevarB(3)
elevarAlaQuinta = elevarA(5)

print(elevarCuadrado(9))
print(elevarCubo(2))
print(elevarCubo(5))


