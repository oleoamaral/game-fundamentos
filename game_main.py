import pygame, time, random

pygame.init()

#NOME DO JOGO E ÍCONE
pygame.display.set_caption("Ainda sem nome")
icon = pygame.image.load("assets/abc.png")
pygame.display.set_icon(icon)

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

while True:
    display.fill((0, 0, 0))
    display.blit(backgroud,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()





    pygame.display.update()
    clock.tick(60)