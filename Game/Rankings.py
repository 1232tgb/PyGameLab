import pygame
import pygameMenu
from DesafioMatematica import Button


BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
def rankingDesafioI(Surface):

    f= open("ranking.txt", "r")
    linhas = f.readlines()
    y = 100
    i= 1
    font = pygame.font.SysFont('Arial', 15)
    msg = font.render("Ranking Desafio Matematica I",True, GREEN)
    colocacao = font.render("Colocação",True, (0, 0, 0))
    pontos = font.render("Pontos",True, (0, 0, 0))
    Surface.blit(msg, (10, 10))
    Surface.blit(colocacao, (10, 50 ))
    Surface.blit(pontos, (100, 50 ))

    for linha in linhas:

        pontuacao = font.render(linha.strip('\n'), True, (0, 0, 0))
        posicao = font.render(str(i), True, (0, 0, 0))
        Surface.blit(pontuacao, (100, y))
        Surface.blit(posicao,(10, y))
        y = y + 50
        i = i + 1


def rankingDesafioII(Surface):

    f= open("ranking2.txt", "r")
    linhas = f.readlines()
    y = 100
    i= 1
    font = pygame.font.SysFont('Arial', 15)
    msg = font.render("Ranking Desafio Matematica II",True, RED)
    colocacao = font.render("Colocação",True, (0, 0, 0))
    pontos = font.render("Pontos",True, (0, 0, 0))
    Surface.blit(msg, (220, 10))
    Surface.blit(colocacao, (220, 50 ))
    Surface.blit(pontos, (310, 50 ))

    for linha in linhas:

        pontuacao = font.render(linha.strip('\n'), True, (0, 0, 0))
        posicao = font.render(str(i), True, (0, 0, 0))
        Surface.blit(pontuacao, (310, y))
        Surface.blit(posicao,(220, y))
        y = y + 50
        i = i + 1


def rankingDesafioIII(Surface):

    f= open("ranking3.txt", "r")
    linhas = f.readlines()
    y = 100
    i= 1
    font = pygame.font.SysFont('Arial', 15)
    msg = font.render("Ranking Desafio Matematica III",True, (0, 0, 0))
    colocacao = font.render("Colocação",True, (0, 0, 0))
    pontos = font.render("Pontos",True, (0, 0, 0))
    Surface.blit(msg, (430, 10))
    Surface.blit(colocacao, (430, 50 ))
    Surface.blit(pontos, (520, 50 ))

    for linha in linhas:

        pontuacao = font.render(linha.strip('\n'), True, (0, 0, 0))
        posicao = font.render(str(i), True, (0, 0, 0))
        Surface.blit(pontuacao, (520, y))
        Surface.blit(posicao,(430, y))
        y = y + 50
        i = i + 1




def jogar():


    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    tela = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    backButton = Button(700, 10, 50, 50, "<")

    while True:
        events =  pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if backButton.isPressed():
                     import menu
                     menu.mainMenu()

        tela.fill((255, 255, 255))
        backButton.draw(tela)

        rankingDesafioI(tela)
        rankingDesafioII(tela)
        rankingDesafioIII(tela)

        pygame.display.update()







if __name__ == '__main__':
    # test1.py executed as script
    # do something
    jogar()
