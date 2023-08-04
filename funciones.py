from principal import *
from configuracion import *
import random
import math


# Selecciona al azar una palabra de la lista
def nuevaPalabra(lista):
    return lista[random.randint(0, len(lista))]

# Lee el archivo, recorre cada linea y verifica que la longitud de la palabra
# sea igual al largo establecido, luego agrega la palabra a la lista correspondiente
def lectura(archivo, salida, largo):
    for palabra in archivo.readlines():
        if len(palabra) == largo + 1:
            salida.append(palabra[:-1].lower())
    return salida

# Si la palabra es correcta, retorna True, en caso de no serlo recorre la palabra letra por letra
# y se fija si cada letra está en la palabra, si está en el indice correcto o si directamente no está
# agregando cada letra a la lista correspondiente
def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    if palabra != palabraCorrecta:
        for indice, letra in enumerate(palabra):
            if letra in palabraCorrecta and palabra[indice] == palabraCorrecta[indice]:
                correctas.append(letra)
            elif letra in palabraCorrecta:
                casi.append(letra)
            else:
                incorrectas.append(letra)
        return False
    return True

# Se define el color que tendrán las letras dependiendo de su estado
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

# Valida si la palabra se encuentra en la lista del diccionario
# la cual solo contiene palabras del lemario y del mismo largo que el establecido
def validacion(palabra, lista_diccionario):
    if palabra in lista_diccionario:
        return True
    return False


# Guarda el último tiempo si el archivo está vacio
# o si es mayor al resto de tiempos
def guardar_tiempo(segundos):
    archivo = open('records.txt', 'r+')
    lista = archivo.readlines()
    if len(lista) == 0:
        archivo.write(str(round(segundos, 1)) + '\n')
    else:
        if segundos > float(max(lista)):
            archivo.write(str(round(segundos, 1)) + '\n')
    archivo.close()

# Lee el archivo de records y devuelve el tiempo máximo que es el record
def obtener_record():
    with open('records.txt', 'r') as archivo:
        lista_records = archivo.readlines()
        if len(lista_records) > 0:
            return max(lista_records)
        else:
            return 0


# Guarda el puntaje si el archivo se encuentra vacio
# o si es mayor a los puntajes guardados
def guardar_puntaje(puntos):
    archivo = open('puntajes.txt', 'r+')
    lista = archivo.readlines()
    if len(lista) == 0:
        archivo.write(str(puntos) + '\n')
    else:
        if puntos > float(max(lista)):
            archivo.write(str(puntos) + '\n')
    archivo.close()

# Lee el archivo de puntajes y devuelve el mas alto
def obtener_puntaje():
    with open('puntajes.txt', 'r') as archivo:
        lista_puntajes = archivo.readlines()
        if len(lista_puntajes) > 0:
            return max(lista_puntajes)
        else:
            return 0
