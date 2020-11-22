import pygame, time, random
from game_functions import *

pygame.init()

#NOME DO JOGO E ÍCONE
name_icon()

#TELA 
largura = 800
altura = 600
display = pygame.display.set_mode((largura,altura))
backgroud = pygame.image.load("assets/fundo.jpg")
clock = pygame.time.Clock()

#LIVRO 
livro = pygame.image.load("assets/livro.png")
livro_largura = 124
livro_X = 360
livro_Y = 460
livro_movi = 0
livro_velo = 10

#LÁPIS
lapis = pygame.image.load("assets/lapis.png")
lapis_largura = 50
lapis_altura = 200
lapis_X = 360
lapis_Y = 10 - lapis_altura
lapis_movi = 0
lapis_velo = 5

#LETRAS
letraA = pygame.image.load("assets/A.png")
letraB = pygame.image.load("assets/B.png")
letraC = pygame.image.load("assets/C.png")
letraD = pygame.image.load("assets/D.png")
letraE = pygame.image.load("assets/E.png")
letraF = pygame.image.load("assets/F.png")
letraG = pygame.image.load("assets/G.png")
letraH = pygame.image.load("assets/H.png")
letraI = pygame.image.load("assets/I.png")
letraJ = pygame.image.load("assets/J.png")
letraK = pygame.image.load("assets/K.png")
letraL = pygame.image.load("assets/L.png")
letraM = pygame.image.load("assets/M.png")
letraN = pygame.image.load("assets/N.png")
letraO = pygame.image.load("assets/O.png")
letraP = pygame.image.load("assets/P.png")
letraQ = pygame.image.load("assets/Q.png")
letraR = pygame.image.load("assets/R.png")
letraS = pygame.image.load("assets/S.png")
letraT = pygame.image.load("assets/T.png")
letraU = pygame.image.load("assets/U.png")
letraV = pygame.image.load("assets/V.png")
letraW = pygame.image.load("assets/W.png")
letraX = pygame.image.load("assets/X.png")
letraY = pygame.image.load("assets/Y.png")
letraZ = pygame.image.load("assets/Z.png")
letra_largura = 70
letra_altura = 70
letra_X = 380
letra_Y = 10 - letra_altura
letra_velo = 5

arquivo = open("dados.txt", "a")
nome = input("Informe seu nome: ")
email = email("Informe seu e-mail: ")
arquivo.write(nome+'\n')
arquivo.write(email+'\n')
arquivo.close()

musica()
contador = 0
while True:
    display.fill((0, 0, 0))
    display.blit(backgroud,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                livro_movi = livro_velo * -1
            elif event.key == pygame.K_RIGHT:
                livro_movi = livro_velo
        if event.type == pygame.KEYUP:
            livro_movi = 0
    livro_X = livro_X + livro_movi 
    if livro_X < 0: 
        livro_X = 0
    elif livro_X > largura - livro_largura:
        livro_X = largura - livro_largura
    display.blit(livro,(livro_X,livro_Y))                    

    lapis_Y = lapis_Y + lapis_velo
    if lapis_Y > altura:
        lapis_Y = 10 - lapis_altura
        lapis_velo = lapis_velo + 0.3
        barulho_lapis()
        lapis_X = random.randrange(0, largura-50)
    display.blit(lapis,(lapis_X,lapis_Y))

    letra_Y = letra_Y + letra_velo
    letras_add = score(contador)
    display.blit(letras_add, (10,10))
    if contador == 0:
        letra = letraA
    elif contador == 1:
        letra = letraB
    elif contador == 2:
        letra = letraC
    elif contador == 3: 
        letra = letraD
    elif contador == 4: 
        letra = letraE
    elif contador == 5: 
        letra = letraF
    elif contador == 6: 
        letra = letraG
    elif contador == 7: 
        letra = letraH
    elif contador == 8: 
        letra = letraI
    elif contador == 9: 
        letra = letraJ
    elif contador == 10: 
        letra = letraK
    elif contador == 11: 
        letra = letraL
    elif contador == 12: 
        letra = letraM
    elif contador == 13: 
        letra = letraN
    elif contador == 14: 
        letra = letraO
    elif contador == 15: 
        letra = letraP
    elif contador == 16: 
        letra = letraQ
    elif contador == 17: 
        letra = letraR
    elif contador == 18: 
        letra = letraS
    elif contador == 19: 
        letra = letraT
    elif contador == 20: 
        letra = letraU
    elif contador == 21: 
        letra = letraV
    elif contador == 22: 
        letra = letraW
    elif contador == 23: 
        letra = letraX
    elif contador == 24: 
        letra = letraY
    elif contador == 25: 
        letra = letraZ
    elif contador == 26: 
        text = ganhou()
        display.blit(text, (100,200))
        pygame.display.update()
        time.sleep(5)
        quit()

    if letra_Y > altura:
        letra_Y = 5 - letra_altura
        letra_velo = letra_velo + 0.5
        letra_X = random.randrange(0, largura)
    display.blit(letra,(letra_X, letra_Y))

    if livro_Y < lapis_Y + lapis_altura:
        if livro_X < lapis_X and livro_X + livro_largura > lapis_X or lapis_X + lapis_largura > livro_X and lapis_X + lapis_largura < livro_X + livro_largura:
            lapis_velo = 5
            lapis_Y = 0 - lapis_altura
            texto = colisao_lapis()
            display.blit(texto,(100,200))
            pygame.display.update()
            time.sleep(5)
            quit()
            
    if livro_Y < letra_Y + letra_altura: 
        if livro_X < letra_X and livro_X + livro_largura > letra_X or letra_X + letra_largura > livro_X and letra_X + letra_largura < livro_X + livro_largura:
            letra_velo = 5
            letra_Y = 0 - letra_altura
            contador += 1
            barulho_letra()
            letra_X = random.randrange(0, largura-70)
            
    pygame.display.update()
    clock.tick(60)