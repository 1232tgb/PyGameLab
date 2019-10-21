import pygame
import pygameMenu
import sys
from pygame.locals import *
from pygameMenu.config import MENU_SELECTED_DRAW
from pygameMenu.examples.game_selector import COLOR_BACKGROUND

import DesafioAlfabeto
import DesafioFormas
import DesafioMatematica

pygame.init()

altura = 600
largura = 800
tela = pygame.display.set_mode((largura, altura))
MENU_BACKGROUND_COLOR = (228, 55, 36)
COR_BRANCA = (255, 255, 255)
COR_AZUL = (0, 0, 255)
COR_VERDE = (0, 255, 0)

clock = pygame.time.Clock()
def main_background():
    bg = pygame.image.load("Imagens/menuBackground.jpg")
    font = pygame.font.Font("Tipografias/Gameplay.ttf", 36)
    text = font.render("Bem Vindo ao Educafun", True,(0,0,0))
    global surface
    tela.blit(bg,(0,0))
    tela.blit(text,((largura*0.5)-(text.get_width()/2),altura*0.1))



main_menu = pygameMenu.Menu(tela,
                                bgfun=main_background,
                                color_selected=COR_BRANCA,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COR_VERDE,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_height=int(600*0.6),
                                menu_width=int(800*0.6),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=True,
                                title='Main menu',
                                draw_select=MENU_SELECTED_DRAW,
                                window_height=600,
                                window_width=800
                                )



def main_background():
    """
    Function used by menus, draw on background while menu is active.
    :return: None
    """
    global surface
    surface.fill(COLOR_BACKGROUND)


##Jogo de matematica
def desafioMatematica():
    DesafioMatematica.jogar()

def desafioAlfabeto():
    DesafioAlfabeto.jogar()

def desafioFormas():

    DesafioFormas.jogar()



main_menu.add_option('Desafio Matematica', desafioMatematica)
main_menu.add_option('Desafio Alfabeto', desafioAlfabeto)
main_menu.add_option('Desafio Formas', desafioFormas)
main_menu.add_option('Sair', pygameMenu.events.EXIT)


def mainMenu(test = False):
    while True:

        events =  pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()
        tela.fill(COR_BRANCA)

        main_menu.draw()

        main_menu.mainloop(events, disable_loop=test)

        # Flip surface

        # At first loop returns
        if test:
            break




            # Clock tick


        pygame.display.update()



mainMenu()



