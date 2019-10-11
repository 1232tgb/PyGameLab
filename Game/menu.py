import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

altura = 600
largura = 800
bg = pygame.image.load("Imagens/menuBackground.jpg")
font = pygame.font.Font("Tipografias/Gameplay.ttf", 36)


screen = pygame.display.set_mode((largura, altura))
text = font.render("Bem Vindo", True,(0,0,0))

background = pygame.Surface(screen.get_size())
background = background.convert()

while 1:
####
    for event in pygame.event.get():
        if event.type == QUIT:
            exit();

    
    screen.blit(bg, (0, 0))
    screen.blit(text,((largura*0.5)-(text.get_width()/2),altura*0.5))
    pygame.display.flip()
####
