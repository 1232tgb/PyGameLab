import pygame
from DesafioMatematica import Button

def fimjogo():


    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    fimdejogoImagem = pygame.image.load("Imagens/gameover2.jpg")
    fimdejogoImagem = pygame.transform.scale(fimdejogoImagem, (800, 600))
    tela = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    backButton = Button(700, 10, 50, 50, "<")
    i = 0
    while i<1:
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
        tela.blit(fimdejogoImagem, (0, 0))

        i = i+1

        pygame.display.update()
        pygame.time.wait(5000)










if __name__ == '__main__':
    # test1.py executed as script
    # do something
    fimjogo()
   # import menu
    #menu.mainMenu()
