import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == 241:
        return("ñ")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SLASH:
        return("-")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


# Funcion que muestra un menu con las dificultades y modos a elegir
def menu(screen):
    #Fuente
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    # Se definen los "checkbox", su color y booleano para cada dificultad y modo de juego
    facil_rect = pygame.Rect(145, 165, 32, 32)
    intermedio_rect = pygame.Rect(145, 265, 32, 32)
    dificil_rect = pygame.Rect(145, 365, 32, 32)
    modo1_rect = pygame.Rect(145, 165, 32, 32)
    modo2_rect = pygame.Rect(145, 365, 32, 32)
    color_inactivo = pygame.Color('lightskyblue3')
    color_activo = pygame.Color('dodgerblue2')
    color_modo1 = color_inactivo
    color_modo2 = color_inactivo
    color_facil = color_inactivo
    color_intermedio = color_inactivo
    color_dificil = color_inactivo
    facil = False
    intermedio = False
    dificil = False
    modo1 = False
    modo2 = False



    while True:
        for event in pygame.event.get():
            
            # Si el usuario presiona en la X, se cierra el juego
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Si el usuario hace click, se verifica si lo hizo en alguna checkbox y se cambia el color
            # y el booleano de esa dificultad
            if event.type == pygame.MOUSEBUTTONDOWN:
                if facil_rect.collidepoint(event.pos):
                    facil = True
                    color_facil = color_activo
                else:
                    facil = False
                    color_facil = color_inactivo

                if intermedio_rect.collidepoint(event.pos):
                    intermedio = True
                    color_intermedio = color_activo
                else:
                    intermedio = False
                    color_intermedio = color_inactivo 

                if dificil_rect.collidepoint(event.pos):
                    dificil = True
                    color_dificil = color_activo
                else:
                    dificil = False
                    color_dificil = color_inactivo    


        # Se pinta el fondo y se imprimen los checkbox y el texto para las dificultades
        screen.blit(pygame.image.load("resources/img/menu_bg.png"), (0,0))

            
        pygame.draw.rect(screen, color_facil, facil_rect)
        screen.blit(defaultFontGrande.render("Fácil", 1, COLOR_LETRAS), (210, 150))

        pygame.draw.rect(screen, color_intermedio, intermedio_rect)
        screen.blit(defaultFontGrande.render("Intermedio", 1, COLOR_LETRAS), (210, 250))

        pygame.draw.rect(screen, color_dificil, dificil_rect)
        screen.blit(defaultFontGrande.render("Difícil", 1, COLOR_LETRAS), (210, 350))



        pygame.display.flip()
        pygame.time.Clock().tick(FPS_inicial)

        # Se verifica qué dificultad se eligió y se cambia el valor de las variables de configuracion.py
        if facil:
            TIEMPO_MAX.append(120)
            LARGO.append(4)
            break
        elif intermedio:
            TIEMPO_MAX.append(80)
            LARGO.append(6)
            break
        elif dificil:
            TIEMPO_MAX.append(30)
            LARGO.append(8)
            break

    # Luego de haber elegido la dificultad, se elige el modo de juego
    while True:
        for event in pygame.event.get():
            
            # Si el usuario presiona en la X, se cierra el juego
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Si el usuario hace click, se verifica en que checkbox de que modo se hizo
            # activando el booleano de este
            if event.type == pygame.MOUSEBUTTONDOWN:
                if modo1_rect.collidepoint(event.pos):
                    modo1 = True
                    color_modo1 = color_activo
                else:
                    modo1 = False
                    color_modo1 = color_inactivo
                    
                if modo2_rect.collidepoint(event.pos):
                    modo2 = True
                    color_modo2 = color_activo
                else:
                    modo2 = False
                    color_modo2 = color_inactivo
                    

        # Se muestra la pantalla para elegir el modo
        screen.blit(pygame.image.load("resources/img/modo_bg.png"), (0,0))

                
        pygame.draw.rect(screen, color_modo1, modo1_rect)
        screen.blit(defaultFontGrande.render("Normal", 1, COLOR_LETRAS), (210, 150))

        pygame.draw.rect(screen, color_modo2, modo2_rect)
        screen.blit(defaultFontGrande.render("Carrera", 1, COLOR_LETRAS), (210, 350))

        pygame.display.flip()
        pygame.time.Clock().tick(FPS_inicial)

        if modo1:
            MODO.append(0)
            break
        elif modo2:
            MODO.append(1)
            break



def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano,
                correctas, incorrectas, casi, palabraCorrecta, ListaCarrera):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    # Verifica en que modo se enceuntra actualmente
    if MODO[-1] == 0:
        # Si está en modo 0, es decir normal, verifica si ganó o no y procede a la pantalla correspondiente
        if gano:
            screen.blit(pygame.image.load("resources/img/gana.png"), (0,0))
            sonido_1 = pygame.mixer.Sound("resources/sonidos/1.mp3")
            pygame.mixer.Sound.play(sonido_1)
            screen.blit(defaultFontGrande.render("Ganaste", 1, COLOR_LETRAS), (250, 270))
            screen.blit(defaultFont.render("La palabra correcta era: " + listaDePalabrasUsuario[-1], 1, COLOR_LETRAS), (250, 405))
            screen.blit(defaultFont.render("Tiempo actual: " + str(round(segundos, 1)) + " segs", 1,  COLOR_LETRAS), (230, 500))
            screen.blit(defaultFont.render("Último mejor tiempo: " + str(obtener_record())[:-1] + " segs", 1, COLOR_LETRAS), (230, 550))
            screen.blit(pygame.image.load("resources/img/back.png"), (20, 500))
            return True
        elif not gano and len(listaDePalabrasUsuario) == INTENTOS or segundos < FPS_inicial/1000:
            screen.blit(pygame.image.load("resources/img/pierde.png"), (0,0))
            sonido_2 = pygame.mixer.Sound("resources/sonidos/2.mp3")
            pygame.mixer.Sound.play(sonido_2)
            screen.blit(defaultFontGrande.render("Perdiste", 1, (232, 17, 35)), (250, 275))
            screen.blit(defaultFont.render("La palabra correcta era: " + palabraCorrecta, 1, (232, 17, 35)), (250, 410))
            screen.blit(pygame.image.load("resources/img/back.png"), (20, 500))
            return False


    # Si el modo es 1, es decir carrera, entra al else
    else:
        # Verifica que se hayan agotado los segundos
        if segundos < FPS_inicial/1000:

            # Muestra la pantalla final correspondiente
            screen.blit(pygame.image.load("resources/img/fin.png"), (0,0))
            screen.blit(defaultFontGrande.render("Fin", 1, COLOR_LETRAS), (330, 275))
            screen.blit(defaultFont.render("Acertaste " + str(puntos) + " palabras", 1, COLOR_LETRAS), (280, 430))
            screen.blit(defaultFont.render("Último record: " + str(obtener_puntaje())[:-1], 1, COLOR_LETRAS), (280, 460))
            screen.blit(pygame.image.load("resources/img/back.png"), (20, 500))
            return False


    # Fondo
    screen.blit(pygame.image.load("resources/img/juego_bg.png"), (0,0))
    
    # Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    # muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (350, 570))

    # muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))

    # muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    # muestra las palabras anteriores, las que se fueron arriesgando
    # si ya hay 6 palabras en pantalla, se limpia la primer palabra en pantalla 
    # para mostrar la ultima sin afectar la lista de palabras del usuario
    pos = 0
    if len(listaDePalabrasUsuario) > 5:
        for palabra in listaDePalabrasUsuario[-5:]:
            screen.blit(defaultFontGrande.render(palabra, 1, COLOR_LETRAS), (ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//4, 20 + 80 * pos))
            pos += 1
    else:
        for palabra in listaDePalabrasUsuario:
            screen.blit(defaultFontGrande.render(palabra, 1, COLOR_LETRAS), (ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//4, 20 + 80 * pos))
            pos += 1

    #muestra el abcdario
    abcdario = ["qwertyuiop", "asdfghjklm", "zxcvbnñ"]
    y=0
    for abc in abcdario:
        x = 0
        for letra in abc:
            # Se le asigna color a las letras dependiendo si son correctas, casi o incorrectas
            color = color_letras(letra, correctas, casi, incorrectas)
            screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
            x += TAMANNO_LETRA
        y += TAMANNO_LETRA








