#Disponemos de una cadena de texto
#Debes Contar las palabras y devolver cuantas veces se repita una de ellas
#La variable se llama texto()


def tolowerCase(text):
    """_summary_

    Args:
        text (cadena de texto): poner en minuscula todas las letras)
    Retorno: cadena en minusculas
    
    """
    
    lowerCase = text.lower()
    return lowerCase

def cleanText(textLower):
    """_Summary

    Args:
        text (cadena de texto): eliminamos puntos y comas, porque pidio contar palabras y no caracteres
    Retorno: cadena solo de palabras
    
    """
    cleanedText = textLower.replace(",", "").replace(".", "")
    
    #separamos cada palabra usando split metiendola en un array
    
    separatedText = cleanedText.split(" ")
    
    return separatedText

def countWords(cleanedText):
    dictionary = {}
    
    #creo bucle for para la busqueda 
   
    for word in cleanedText:
        
        if word in dictionary:
            dictionary [word] += 1
        else:
            dictionary [word] = 1
            
    return dictionary 
    

text= "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar"

lowerCase = tolowerCase(text)

cleanedText = cleanText(lowerCase)

countedWords = countWords(cleanedText)

print(countedWords)