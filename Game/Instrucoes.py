import pygame

from DesafioMatematica import Button

def blit_text(Surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = Surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            Surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def jogar():

    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    tela = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    backButton = Button(700, 10, 50, 50, "<")
    bg = pygame.image.load("Imagens/menuBackground.jpg")
    font = pygame.font.SysFont("Arial", 24)
    text = "Instruções:" \
           "\nCaminhe com o avatar em direção a resposta correta" \
           "\nQuando acertar o quadradinho ficará verde e você ganhará 5 pontos, quando errar o botão ficará vermelho e você não ganhará pontos" \
           "\nDesafio de Matematica I: Nesse nivel você realiza operações de soma simples." \
           "\nDesafio de Matematica II: Nesse nivel você realiza operações de multiplicação e divisão." \
           "\nDesafio de Matematica III: Nesse nivel você realiza as 4 operações fundamentais da matematica: Soma, Subtração, Divisão e Multiplicação" \
           "\nComandos:" \
           "\nW: para cima S: para baixo D: para a direita A: para a esquerda" \


    while True:
        events =  pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if backButton.isPressed():
                import menu
                menu.mainMenu()

        tela.fill((255, 255, 255))
        tela.blit(bg,(0,0))
        blit_text(tela, text, (100, 100), font)
        backButton.draw(tela)
        pygame.display.update()



if __name__ == '__main__':
    # test1.py executed as script
    # do something
    jogar()
