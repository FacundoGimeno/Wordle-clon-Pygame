#! /usr/bin/env python
import os
import random
import sys
import math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *

from funcionesVACIAS import *

# Funcion principal

def main():

        # Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        icon = pygame.image.load("resources/img/icon.png")
        pygame.display.set_icon(icon)

        # Preparar la ventana
        pygame.display.set_caption("La escondida...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        # Fuentes
        defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
        defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

        # Carga la música y se establece el volumen
        pygame.mixer.music.load("resources/sonidos/bgmusic.mp3")
        pygame.mixer.music.set_volume(0.2)
        
        # Se verifica si la musica ya está siendo reproducida, si no se reproduce
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(1)

        # Se muestra el menu con selector de dificultad
        menu(screen)
        
        # tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX[-1]
        largo = LARGO[-1]
        fps = FPS_inicial

        puntos = 0
        palabraUsuario = ""
        listaPalabrasDiccionario = []
        ListaDePalabrasUsuario = []
        ListaCarrera = []
        correctas = []
        incorrectas = []
        casi = []
        gano = False
        control = True
        repetido = False


        
        archivo = open("lemario.txt", "r")
        # lectura del diccionario
        lectura(archivo, listaPalabrasDiccionario, largo)

        # elige una al azar
        palabraCorrecta = nuevaPalabra(listaPalabrasDiccionario)

        # Dibuja la pantalla
        dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano, correctas, incorrectas, casi, palabraCorrecta, ListaCarrera)
        
        print(palabraCorrecta)

        intentos = 5
        while segundos > fps/1000 and intentos > 0 and not gano:

        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()
            if True:
                fps = 3
            
            # Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                # QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return ()

                # Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra  # es la palabra que escribe el usuario

                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]

                    if e.key == K_RETURN:
                        repetido = False

                        # Valida que la palabra esté en el lemario y que sea del mismo largo
                        # cambia el booleano control
                        if validacion(palabraUsuario, listaPalabrasDiccionario) == True:                        
                            control = True


                            # Valida que la palabra no sea repetida, en caso de serlo cambia el booleano a True
                            # y se salta el if para que la palabra no se agregue a la lista
                            if palabraUsuario in ListaDePalabrasUsuario:
                                repetido = True
                                continue
                            ListaDePalabrasUsuario.append(palabraUsuario)

                            # Luego verifica en que modo se está jugando, si normal o carrera
                            # y realiza las acciones deseadas para cada modo
                            if MODO[-1] == 0:
                                intentos -= 1
                                gano = revision(palabraCorrecta, palabraUsuario, correctas, incorrectas, casi)
                            else:
                                if revision(palabraCorrecta, palabraUsuario, correctas, incorrectas, casi):
                                    ListaCarrera.append(palabraCorrecta)
                                    puntos += 1
                                    ListaDePalabrasUsuario = []
                                    correctas = []
                                    casi = []
                                    incorrectas = []
                                    sonido_1 = pygame.mixer.Sound("resources/sonidos/1.mp3")
                                    pygame.mixer.Sound.play(sonido_1)
                                    palabraCorrecta = nuevaPalabra(listaPalabrasDiccionario)
                                    print(palabraCorrecta)
                        else:
                            control = False
                        palabraUsuario = ""
                
            
            # Se actualizan los segundos
            segundos = TIEMPO_MAX[-1] - totaltime/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos,segundos, gano, correctas, incorrectas, casi, palabraCorrecta, ListaCarrera)

            # Verifica los booleanos control y repetido e imprime los mensajes correspondientes
            if control == False:
                screen.blit(defaultFont.render(f"No está en el lemario o su longitud es diferente a ({largo})", 1, (255, 255, 255)), (190, 540))
        
            if repetido:
                screen.blit(defaultFont.render("Ya ingresó esta palabra", 1, (255, 255, 255)), (190, 540))
            
            pygame.display.flip()

            





        # Guarda el tiempo para los records en caso del modo normal
        # Si no guarda el puntaje en modo carrera
        if MODO[-1] == 0:
            guardar_tiempo(segundos)
        else:
            guardar_puntaje(puntos)
        
        # Crea una flecha para volver al menu y espera a que el usuario la presione
        # o salga del juego
        back_rect = pygame.Rect(20, 500, 100, 100)
        

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

                # Si el usuario hace click sobre la flecha, vuelve al menu
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(e.pos):
                        main()
        

        archivo.close()
#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
