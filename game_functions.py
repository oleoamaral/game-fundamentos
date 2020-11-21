import pygame, time

def colisao_lapis():
    font = pygame.font.SysFont(None,150)
    text = font.render("Você morreu!", True, (22, 100, 132))

    return text

def score(contador):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Letras Coletas: "+str(contador), True, (22, 100, 132))
    
    return text

def ganhou():
    font = pygame.font.SysFont(None, 150)
    text = font.render("Parabéns!", True, (22, 100, 132))
    
    return text

