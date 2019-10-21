import pygame

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
font = pygame.font.Font(None,65)
score_font = pygame.font.SysFont("comicsansms", 72)



tela = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def jogar():

    pygame.display.update()



if __name__ == '__main__':

    jogar()

