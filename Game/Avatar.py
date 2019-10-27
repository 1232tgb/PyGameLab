import pygame
import pygameMenu
import sys
from pygame.locals import *
from pygameMenu.config import MENU_SELECTED_DRAW
from pygameMenu.examples.game_selector import COLOR_BACKGROUND
from pygame import event
class Avatar:
    def __init__(self, imagem, nome, posx, posy):
        self.imagem = imagem
        self.score = 0
        self.nome = nome
        self.posx = posx
        self.posy = posy
        self.andar = False


    def movimentar(self):
        v = pygame.Vector2()
        keys= pygame.key.get_pressed()

        if keys[K_d]:

            self.posx = +1
        if keys[K_a]:
            self.posy = -1



    def desenhar(self, surface):
        surface.blit(self.imagem, (self.posx, self.posy))
