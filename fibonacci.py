'''La sucesión de fibonacci empieza con los numeros 0 y 1
a prtir de esto cada elemento es la suma de los dos numeros anteriores'''

#f(x) = f(x-1) = f(x-2)

''''''
#definimos al señor fibonacci


'''Pero como minimizar la compllejidad, la cantidad de pasos que tiene
que ejecutar este programa?
Usemos un dicionario!! Una hashtable!
'''


fibo_dict = dict()


def fibo(num: int) -> int:
    if num == 1 or num == 0: #Recursividad!!!  por eso usamos un dcitionary
        print(f'{num} -> 1')
        return 1
    elif num < 0:
        raise Exception(" mmmna ta roto!")
    
    if num in fibo_dict:
        print(f'{num} en dict')
        return fibo_dict[num]
    
    print(f'{num} -> {num-1}, {num-2}')
    res = fibo(num-1) + fibo(num-2)
    fibo_dict[num] = res
    return res


numero = 8
res = fibo(numero)
print(f'fibo(numero) == {res}')



