import re
from colorama import Fore
import requests

#defino url a scrappear
website ="https://www.vulnhub.com/"

resultado = requests.get(website)
content = resultado.text


#creando un patrón de busqueda por titulos

patron = r"/entry [ \w-]*"

maquinas_repetidas = re.findall(patron, str(content))

print(maquinas_repetidas)

sin_duplicados = list(set(maquinas_repetidas))
print(sin_duplicados)

#creando la lista y almacenar

maquinas_final = []
for i in sin_duplicados:
    nombre_maquinas = i.replace("/entry/", "")
    maquinas_final.append(nombre_maquinas)

    print(nombre_maquinas)


#Condicional para saber si la maquina noob cambio y se agrego algo mas 

maquina_noob = "noob-1" #Cambiar este valor por cualquier otro para probar el condicional y el color 
existe_noob = False

for a in maquinas_final:
    if a == maquina_noob:
        existe_noob = True
        break
color_verde = Fore.GREEN
color_blue = Fore.BLUE


if existe_noob == True:
    print("\n" + color_verde + "No hay ningua maquina nueva")
else:
    print("\n" + color_blue + "Maquina nueva encontrada")
