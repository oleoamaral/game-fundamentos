import pygame, time

def colisao_lapis():
    font = pygame.font.SysFont(None,150)
    text = font.render("Você morreu", True, (22, 100, 132))

    return text

def score(contador):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Letras Coletas: "+str(contador), True, (22, 100, 132))
    
    return text

def ganhou():
    font = pygame.font.SysFont(None, 150)
    text = font.render("Parabéns!", True, (22, 100, 132))
    
    return text

def barulho_letra():
    som_letra = pygame.mixer.Sound("assets/somlivro.wav")
    som_letra.set_volume(0.5)
    pygame.mixer.Sound.play(som_letra)

def musica():
    pygame.mixer.music.load("assets/musica.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

def barulho_lapis():
    som_lapis = pygame.mixer.Sound("assets/somlapis.wav")
    som_lapis.set_volume(0.1)
    pygame.mixer.Sound.play(som_lapis)

def email(mensagem):
    while True:
        valor = input(mensagem)
        if "@" in valor:
            return valor
            break
        else:
            print("Valor informado incorretamente!")

def name_icon():
    pygame.display.set_caption("Ainda sem nome")
    icon = pygame.image.load("assets/abc.png")
    pygame.display.set_icon(icon)

