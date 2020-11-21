import pygame, time

def colisao_lapis():
    font = pygame.font.SysFont(None,150)
    text = font.render("Você morreu!", True, (0,0,0))

    return text