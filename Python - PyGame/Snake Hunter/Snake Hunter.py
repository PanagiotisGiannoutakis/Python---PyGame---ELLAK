import pygame, sys
from pygame.locals import *
from random import *

RED = (255, 0 , 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0 , 255)
GREEN = (0, 255, 0)

colorList = [RED, BLACK, BLUE, WHITE, PINK, GREEN]



class Target():

    def __init__(self, my_window, listRect, pixelAreaX, pixelAreaY):
        collide = True
        while collide:
            choice_pixelX = randint(0, len(pixelAreaX)-1)
            choice_pixelY = randint(0, len(pixelAreaY)-1)
            self.rect = pygame.Rect((pixelAreaX[choice_pixelX], pixelAreaY[choice_pixelY]), (30, 30))
            for rect in listRect:
                if not self.rect.colliderect(rect):
                    collide = False
                else:
                    collide = True
                    break
        pygame.draw.rect(my_window, YELLOW, self.rect, 0)

    def drawAgain(self, my_window):
        pygame.draw.rect(my_window, YELLOW, self.rect, 0)

class Snake():

    def __init__(self, speedX, speedY, my_window, pixelAreaX, pixelAreaY):
        self.speedX = speedX
        self.speedY = speedY
        self.listRect = []
        self.listRect.append(pygame.Rect((60, 60), (30, 30)))
        pygame.draw.rect(my_window, RED, self.listRect[0], 0)
        self.lose = False
        self.beforeMove = 3
        self.moveAction = 3
        self.correctDirection = 0

    def move(self, my_window):
        turnX = self.listRect[0].left
        turnY = self.listRect[0].top
        if self.moveAction == 1:
            for i in range(len(self.listRect)):
                if self.listRect[i].left == turnX and self.listRect[i].top == turnY:
                    self.listRect[i].move_ip(-self.speedX, 0)
                    pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    self.correctDirection += 1
                else:
                    if self.beforeMove == 1:
                        self.listRect[i].move_ip(-self.speedX, 0)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 2:
                        self.listRect[i].move_ip(0, -self.speedY)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 3:
                        self.listRect[i].move_ip(self.speedX, 0)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 4:
                        self.listRect[i].move_ip(0, self.speedY)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                        
        elif self.moveAction == 2:
            for i in range(len(self.listRect)):
                if self.listRect[i].left == turnX and self.listRect[i].top == turnY:
                    self.listRect[i].move_ip(0, -self.speedY)
                    pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                else:
                    if self.beforeMove == 1:
                        self.listRect[i].move_ip(-self.speedX, 0)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 2:
                        self.listRect[i].move_ip(0, -self.speedY)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 3:
                        self.listRect[i].move_ip(self.speedX, 0)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 4:
                        self.listRect[i].move_ip(0, self.speedY)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                        
        elif self.moveAction == 3:
            for i in range(len(self.listRect)):
                if self.listRect[i].left == turnX and self.listRect[i].top == turnY:
                    self.listRect[i].move_ip(self.speedX, 0)
                    pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                else:
                    if self.beforeMove == 1:
                        self.listRect[i].move_ip(-self.speedX, 0)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 2:
                        self.listRect[i].move_ip(0, -self.speedY)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 3:
                        self.listRect[i].move_ip(self.speedX, 0)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 4:
                        self.listRect[i].move_ip(0, self.speedY)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                        
        elif self.moveAction == 4:
            for i in range(len(self.listRect)):
                if self.listRect[i].left == turnX and self.listRect[i].top == turnY:
                    self.listRect[i].move_ip(0, self.speedY)
                    pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                else:
                    if self.beforeMove == 1:
                        self.listRect[i].move_ip(-self.speedX, 0)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 2:
                        self.listRect[i].move_ip(0, -self.speedY)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 3:
                        self.listRect[i].move_ip(self.speedX, 0)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                    elif self.beforeMove == 4:
                        self.listRect[i].move_ip(0, self.speedY)
                        pygame.draw.rect(my_window, RED, self.listRect[i], 0)
                
        self.checkForBorders(my_window)

    def checkForBorders(self, my_window):
        if self.listRect[0].bottom > my_window.get_height():
            self.speedX = 0
            self.speedY = 0
            self.lose = True
        if self.listRect[0].top < 0:
            self.speedX = 0
            self.speedY = 0
            self.lose = True
        if self.listRect[0].left < 0:
            self.speedX = 0
            self.speedY = 0
            self.lose = True
        if self.listRect[0].right > my_window.get_width():
            self.speedX = 0
            self.speedY = 0
            self.lose = True

def main():

    pygame.init()

    pygame.mixer.music.load('aaa.mp3')
    pygame.mixer.music.play(-1)

    dimensions = (810, 570)

    my_window = pygame.display.set_mode(dimensions)
    pygame.display.set_caption('Snake Snake Snake !!!')

    my_background = pygame.image.load('background.png')
    my_window.blit(my_background, (0,0))

    my_clock = pygame.time.Clock()

    pixelAreaX = []

    for i in range(0, 780, 30):
        pixelAreaX.append(i)

    pixelAreaY = []

    for j in range(0, 540, 30):
        pixelAreaY.append(j)

    my_snake = Snake(30, 30, my_window, pixelAreaX, pixelAreaY)
    
    continueMove = True
    
    my_snake.move(my_window)
    
    my_target = Target(my_window, my_snake.listRect, pixelAreaX, pixelAreaY)
    
    while True:

        my_background = pygame.image.load('background.png')
        my_window.blit(my_background, (0,0))

        my_target.drawAgain(my_window)
        
        if not continueMove:
            continueMove = True
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif ev.key == K_LEFT and not my_snake.beforeMove == 3:
                    my_snake.correctDirection = 0
                    my_snake.moveAction = 1
                    my_snake.move(my_window)
                    my_snake.beforeMove = 1
                    continueMove = False
                elif ev.key == K_UP and not my_snake.beforeMove == 4:
                    my_snake.correctDirection = 0
                    my_snake.moveAction = 2
                    my_snake.move(my_window)
                    my_snake.beforeMove = 2
                    continueMove = False
                elif ev.key == K_RIGHT and not my_snake.beforeMove == 1:
                    my_snake.correctDirection = 0
                    my_snake.moveAction = 3
                    my_snake.move(my_window)
                    my_snake.beforeMove = 3
                    continueMove = False
                elif ev.key == K_DOWN and not my_snake.beforeMove == 2:
                    my_snake.correctDirection = 0
                    my_snake.moveAction = 4
                    my_snake.move(my_window)
                    my_snake.beforeMove = 4
                    continueMove = False

        if my_snake.moveAction == 1 and continueMove:
                my_snake.move(my_window)
        elif my_snake.moveAction == 2 and continueMove:
                my_snake.move(my_window)
        elif my_snake.moveAction == 3 and continueMove:
                my_snake.move(my_window)
        elif my_snake.moveAction == 4 and continueMove:
                my_snake.move(my_window)

        if my_snake.listRect[0].colliderect(my_target):
            my_target = Target(my_window, my_snake.listRect, pixelAreaX, pixelAreaY)
            if my_snake.moveAction == 1:
                my_snake.listRect.insert(0, pygame.Rect((my_snake.listRect[0].left - 30, my_snake.listRect[0].top), (30, 30)))
            elif my_snake.moveAction == 2:
                my_snake.listRect.insert(0, pygame.Rect((my_snake.listRect[0].left, my_snake.listRect[0].top - 30), (30, 30)))
            elif my_snake.moveAction == 3:
                my_snake.listRect.insert(0, pygame.Rect((my_snake.listRect[0].left + 30, my_snake.listRect[0].top), (30, 30)))
            elif my_snake.moveAction == 4:
                my_snake.listRect.insert(0, pygame.Rect((my_snake.listRect[0].left, my_snake.listRect[0].top + 30), (30, 30)))
            pygame.draw.rect(my_window, RED, my_snake.listRect[0], 0)
        
        if my_snake.lose == True:
            my_font = pygame.font.SysFont('Arial Black', 60)
            my_text = my_font.render('You Lose !!!', False, WHITE)
            my_window.blit(my_text, ((my_window.get_width()-my_text.get_width())/2, (my_window.get_height()-my_text.get_height())/2))
            pygame.mixer.music.stop()
            pygame.mixer.music.load('bbb.mp3')
            pygame.mixer.music.play(0)
            pygame.time.wait(5000)

            
        pygame.display.update()

        my_clock.tick(4)
        
if __name__ == '__main__':
	main()
