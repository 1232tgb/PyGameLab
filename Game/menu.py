import pygame
import pygameMenu
import sys
from pygame.locals import *
from pygameMenu.config import MENU_SELECTED_DRAW
from pygameMenu.examples.game_selector import COLOR_BACKGROUND

import Instrucoes
import Rankings
from Avatar import Avatar

import DesafioMatematicaTres
import DesafioMatematicaDois
import DesafioMatematica

class LigaSom:

    def __init__(self):
       self.somLigado = False
<<<<<<< HEAD
       self.somRaposa = True

=======
>>>>>>> 05b86bde4bc48826badef1c7c2a6aef9e47eb416



pygame.init()

altura = 600
largura = 800
tela = pygame.display.set_mode((largura, altura))
MENU_BACKGROUND_COLOR = (228, 55, 36)
COR_BRANCA = (255, 255, 255)
COR_AZUL = (0, 0, 255)
pygame.mixer.music.load("backGroundSong.mp3")
pygame.mixer.music.play(-1)



<<<<<<< HEAD

=======
>>>>>>> 05b86bde4bc48826badef1c7c2a6aef9e47eb416
COR_VERDE = (0, 255, 0)
avatarImagem = pygame.image.load("imagens/bruno.png")

somLigado = LigaSom()

clock = pygame.time.Clock()
def main_background():
    bg = pygame.image.load("Imagens/mathBackground.jpg")
    bg = pygame.transform.scale(bg, (800, 600))
    font = pygame.font.Font("Tipografias/Gameplay.ttf", 36)
    text = font.render("Bem Vindo ao Funact", True,(0,0,0))
    global surface
    tela.blit(bg,(0,0))
    tela.blit(text,((largura*0.5)-(text.get_width()/2),altura*0.05))



main_menu = pygameMenu.Menu(tela,
                                bgfun=main_background,
                                color_selected=COR_BRANCA,
                                font=pygameMenu.font.FONT_OPEN_SANS,
                                font_color=COR_VERDE,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_height=int(600*0.7),
                                menu_width=int(800*0.7),
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
    avatar = Avatar(avatarImagem, "Bruno", 10, 10)
    DesafioMatematica.jogar(somLigado.somRaposa)


def desafioMatematicaDois():
    DesafioMatematicaDois.jogar(somLigado.somRaposa)

def desafioMatematicaTres():

    DesafioMatematicaTres.jogar(somLigado.somRaposa)

def opcoesJogo():

    Instrucoes.jogar()

def ranking():

    Rankings.jogar()


def liga_desliga_som(LigaSom):

    if LigaSom.somLigado == False:
        pygame.mixer.music.pause()
        LigaSom.somLigado= True


<<<<<<< HEAD

    elif LigaSom.somLigado == True:
        pygame.mixer.music.unpause()

        LigaSom.somLigado = False


    if LigaSom.somRaposa == True:
        LigaSom.somRaposa = False

    elif LigaSom.somRaposa == False:
        LigaSom.somRaposa = True



=======
    elif LigaSom.somLigado == True:
        pygame.mixer.music.unpause()
        LigaSom.somLigado = False


>>>>>>> 05b86bde4bc48826badef1c7c2a6aef9e47eb416


main_menu.add_option('Desafio Matematica', desafioMatematica)
main_menu.add_option('Desafio Matematica II', desafioMatematicaDois)
main_menu.add_option('Desafio Matematica III', desafioMatematicaTres)
main_menu.add_option('Instruções', opcoesJogo)
main_menu.add_option('Rankings', ranking)
main_menu.add_option('Ligar/Desligar som', liga_desliga_som, somLigado)
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



