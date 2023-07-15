'''Definir una funcion max que tome como argumento dos numeros
y devuelva el mayor de ellos. Es cierto que python tiene una funcion max() incorporada
pero hay que hacerla vos mismo'''

def numMayor(n1: int, n2: int):
    
    """[summary]
     "Dados dos numeros de entrada retorna el maximo de ambos
    Args:
        n1 (int): description
        n2 (int): description
    returns:
         [type]: description
            
    """
    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    elif n1 == n2:
        raise Exception("Los valores son iguales")
    raise Exception("Algo ha salido mal")

print(numMayor(1, 2))
print(numMayor(3,2))
   

"""Definir una funcion max_de_tres(), que tome tres numeros como argumentos y
   devuelva el mayor"""
   
def max_de_tres(n1, n2, n3):
    """[summary]

    Args:
        n1 (int_): Primero a comparar
        n2 (int_): Segundo a comparar
        n3 (int): Tercero a comparar
        
    Returns: Retorna el mayor de ellos
    """
    """Pensemos que los tres numeros a, b y c
    
    a > b > c
    b > c
    a > c """
    
    n = numMayor(n1,n2)
    n_final = numMayor(n3, n)
    
    return n_final