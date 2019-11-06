import random
from pygame import event
import pygame
import Avatar


from pygame.locals import *
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

a = random.randint(0,100)
b = random.randint(0,100)



class DesafioMatDois:

    def __init__(self):


        self.score = 0
        self.problem = {"num1":0,"num2":0,"result":0}
        self.button_list = self.get_button_list()
        self.reset_problem = False

        self.sound_1 = pygame.mixer.Sound("item1.ogg")
        self.sound_2 = pygame.mixer.Sound("item2.ogg")
        self.backButton = Button(700, 10, 50, 50, "<")
        self.operation = ""
        self.vilao = pygame.image.load("Imagens/vilao3.jpg")
        self.apareceVilao = False

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


    def multiplication(self):
        """ These will set num1,num2,result for multiplication """
        a = random.randint(0,12)
        b = random.randint(0,12)
        self.problem["num1"] = a
        self.problem["num2"] = b
        self.problem["result"] = a * b
        self.button_list = self.get_button_list()
        self.operation = "x"
    def division(self):
        """ These will set num1,num2,result for division """
        divisor = random.randint(1,12)
        dividend = divisor * random.randint(1,12)
        quotient = dividend / divisor
        self.problem["num1"] = dividend
        self.problem["num2"] = divisor
        self.problem["result"] = quotient
        self.button_list = self.get_button_list()
        self.operation = ":"

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
        operacao = font.render(self.operation,True,BLACK)

                # t_w: total width
        t_w = label_1.get_width() + label_2.get_width() + 64 # 64: length of symbol
        posX = (SCREEN_WIDTH / 2) - (t_w / 2)
        tela.blit(label_1,(posX,50))

        tela.blit(label_2,(posX + label_1.get_width() + 64,50))
        tela.blit(operacao,(posX+label_1.get_width()/2+32,50))
        if self.reset_problem:
            proxOperacao= random.randint(1,2)
            pygame.time.wait(1000)
            if proxOperacao==1:
                self.multiplication()
            else:
                self.division()
            self.reset_problem = False

    def checa_resultado(self, posx, posy, Sound, ligaSom):

        for button in self.button_list:

            if posx>=button.x and posx<=button.x+button.width and posy>=button.y and posy<=button.y+button.height:
                if button.get_number() == self.problem["result"]:
                    button.set_color(GREEN)

                    self.score += 5
                    self.sound_1.play()
                    self.apareceVilao = False
                    self.reset_problem=True

                else:

                    button.set_color(RED)
                    self.sound_1.play()
                    self.apareceVilao = True
                    if ligaSom == True:
                        Sound.play()
                        print("ola")
                    self.reset_problem=True
                    self.reset_problem=True

    def backButton_isPressed(self):

       if self.backButton.isPressed():
           f= open("ranking2.txt","a+")
           f.write(str(self.score)+"\n")
           f.close()
           import gameover
           gameover.fimjogo()
           import menu
           menu.mainMenu()


class Button(object):
        def __init__(self,x,y,width,height,number):
            self.rect = pygame.Rect(x,y,width,height)
            self.font = pygame.font.Font(None,40)
            self.text = self.font.render(str(number),True,BLACK)
            self.number = number
            self.background_color = WHITE
            self.x = x
            self.y = y
            self.width = width
            self.height = height

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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
font = pygame.font.Font(None,65)
score_font = pygame.font.SysFont("comicsansms", 72)
avatarImagem = pygame.image.load("Imagens/bruno.png")





tela = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


def jogar(somRaposa):
    tela = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    score = 0
    desafioMatematica = DesafioMatDois()
    desafioMatematica.division()
    clock = pygame.time.Clock()

    counter, text = 0, '0'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    posX=10
    posY=200


    while True:


        events =  pygame.event.get()
        for event in events:
            if event.type == pygame.USEREVENT:
                counter += 1
                text = str(counter).rjust(3)
                if event.type == pygame.QUIT: break


            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                desafioMatematica.check_result()
                desafioMatematica.backButton_isPressed()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    posX = posX +15
                if event.key == pygame.K_a:
                    posX =posX -15
                if event.key == pygame.K_s:
                    if posY>=SCREEN_HEIGHT :

                        posY= posY -60

                    posY =posY +15

                if event.key == pygame.K_w:
                    posY =posY -15
        tela.fill(WHITE)
        tela.blit(avatarImagem, (posX,posY ))
        desafioMatematica.backButton.draw(tela)
        tela.blit(font.render(text, True, (0, 0, 0)), (32, 48))

        somVilao = pygame.mixer.Sound("villainlaugh2.ogg")

        if desafioMatematica.apareceVilao == True:
            tela.blit(desafioMatematica.vilao,(650, 450))

        desafioMatematica.checa_resultado(posX, posY, somVilao, somRaposa)



        if desafioMatematica.reset_problem==True:
            posX=10
            posY=200

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
