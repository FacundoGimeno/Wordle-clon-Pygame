from principal import *
from configuracion import *
import random
import math



def nuevaPalabra(lista):
    return lista[random.randint(0, len(lista))]

def lectura(archivo, salida, largo):
    for palabra in archivo.readlines():
        if len(palabra) == largo:
            salida.append(palabra)
    return salida

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    palabra += '\n'
    if palabra != palabraCorrecta:
        for indice, letra in enumerate(palabra):
            if letra in palabraCorrecta and palabra[indice] == palabraCorrecta[indice]:
                correctas.append(letra)
            elif letra in palabraCorrecta:
                casi.append(letra)
            else:
                incorrectas.append(letra)

    elif palabra == palabraCorrecta:
        return True
    return False

def color_letras(letra, correctas, casi, incorrectas):
    if letra in correctas:
        color = COLOR_LETRAS
    elif letra in casi:
        color = (33, 159, 213)
    elif letra in incorrectas:
        color = (232, 17, 35)
    else:
        color = (255, 255, 255)
    return color

#def validacion(palabra, largo, lemario):
#    while palabra not in lemario or len(palabra) != largo:
#        pass
#    return palabra