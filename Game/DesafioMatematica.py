import random

import pygame


BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

a = random.randint(0,100)
b = random.randint(0,100)



class DesafioMat:

    def __init__(self):

        self.reset_problem = False
        self.score = 0
        self.problem = {"num1":0,"num2":0,"result":0}
        self.button_list = self.get_button_list()


    def check_result(self):
        """ Check the result """
        for button in self.button_list:
            if button.isPressed():
                if button.get_number() == self.problem["result"]:
                    # set color to green when correct
                    button.set_color(GREEN)
                    # increase score
                    self.score += 5
                    # Play sound effect

                else:
                    # set color to red when incorrect
                    button.set_color(RED)
                    # play sound effect

                # Set reset_problem True so it can go to the
                # next problem
                # we'll use reset_problem in display_frame to wait
                # a second
                self.reset_problem = True

    def addition(self):

        a = random.randint(0,100)
        b = random.randint(0,100)
        self.problem["num1"] = a
        self.problem["num2"] = b
        self.problem["result"] = a + b
        self.button_list = self.get_button_list()
        self.operation = "addition"

    def get_button_list(self):
            """ Return a list with four buttons """
            button_list = []
            # assign one of the buttons with the right answer
            choice = random.randint(1,4)
            # define the width and height
            width = 100
            height = 100
            # t_w: total width
            t_w = width * 2 + 50
            posX = (SCREEN_WIDTH / 2) - (t_w /2)
            posY = 150
            if choice == 1:
                btn = Button(posX,posY,width,height, self.problem["result"])
                button_list.append(btn)
            else:
                btn = Button(posX,posY,width,height,random.randint(0,100))
                button_list.append(btn)

            posX = (SCREEN_WIDTH / 2) - (t_w/2) + 150

            if choice == 2:
                btn = Button(posX,posY,width,height,self.problem["result"])
                button_list.append(btn)
            else:
                btn = Button(posX,posY,width,height,random.randint(0,100))
                button_list.append(btn)

            posX = (SCREEN_WIDTH / 2) - (t_w /2)
            posY = 300


            if choice == 3:
                btn = Button(posX,posY,width,height, self.problem["result"])
                button_list.append(btn)
            else:
                btn = Button(posX,posY,width,height,random.randint(0,100))
                button_list.append(btn)

            posX = (SCREEN_WIDTH / 2) - (t_w/2) + 150

            if choice == 4:
                btn = Button(posX,posY,width,height, self.problem["result"])
                button_list.append(btn)
            else:
                btn = Button(posX,posY,width,height,random.randint(0,100))
                button_list.append(btn)

            return button_list

    def display_frame(self,tela):

        label_1 = font.render(str(self.problem["num1"]),True,BLACK)
        label_2 = font.render(str(self.problem["num2"])+" = ?",True,BLACK)
        operacao = font.render("+",True,BLACK)

                # t_w: total width
        t_w = label_1.get_width() + label_2.get_width() + 64 # 64: length of symbol
        posX = (SCREEN_WIDTH / 2) - (t_w / 2)
        tela.blit(label_1,(posX,50))


        tela.blit(label_2,(posX + label_1.get_width() + 64,50))
        tela.blit(operacao,(260,40))
        if self.reset_problem:
            # wait 1 second
            pygame.time.wait(1000)
            self.addition()
            self.reset_problem = False


class Button(object):
        def __init__(self,x,y,width,height,number):
            self.rect = pygame.Rect(x,y,width,height)
            self.font = pygame.font.Font(None,40)
            self.text = self.font.render(str(number),True,BLACK)
            self.number = number
            self.background_color = WHITE

        def draw(self,screen):
            """ This method will draw the button to the screen """
            # First fill the screen with the background color
            pygame.draw.rect(screen,self.background_color,self.rect)
            # Draw the edges of the button
            pygame.draw.rect(screen,BLACK,self.rect,3)
            # Get the width and height of the text surface
            width = self.text.get_width()
            height = self.text.get_height()
            # Calculate the posX and posY
            posX = self.rect.centerx - (width / 2)
            posY = self.rect.centery - (height / 2)
            # Draw the image into the screen
            screen.blit(self.text,(posX,posY))



        def isPressed(self):
            """ Return true if the mouse is on the button """
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                return True
            else:
                return False

        def set_color(self,color):
            """ Set the background color """
            self.background_color = color

        def get_number(self):
            """ Return the number of the button."""
            return self.number

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
font = pygame.font.Font(None,65)
score_font = pygame.font.SysFont("comicsansms", 72)



tela = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
def jogar():
    tela = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    score = 0
    desafioMatematica = DesafioMat()
    desafioMatematica.addition()
    clock = pygame.time.Clock()
    while True:


        events =  pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                desafioMatematica.check_result()
        tela.fill(WHITE)


        for btn in desafioMatematica.button_list:

            btn.draw(tela)

            score_label = font.render("Pontuação:"+str(desafioMatematica.score), True, (0, 128, 0))
            tela.blit(score_label,(10,10))

        pygame.time.wait(200)
        desafioMatematica.display_frame(tela)




        pygame.display.update()



if __name__ == '__main__':
    # test1.py executed as script
    # do something
    jogar()
