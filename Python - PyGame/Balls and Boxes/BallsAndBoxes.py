import pygame, sys, random, time, math
from pygame.locals import *
from pygame.sprite import *

pygame.init()

class Ball(Sprite):
    def __init__(self, createX, createY, dimX=100, dimY=100, speedX=5, speedY=5):
        Sprite.__init__(self)   
        self.rect = pygame.Rect(createX, createY, dimX, dimY)
        self.speedX = speedX
        self.speedY = speedY
        self.status = False
        
        
    def draw(self, surf):
        self.highlight = self.rect.collidepoint(pygame.mouse.get_pos())
        if not self.status:
            if not self.highlight:
                self.image = pygame.image.load('ball.png')
                surf.blit(self.image, self.rect)
            elif self.highlight and pygame.mouse.get_pressed()[0]:
                self.image = pygame.image.load('ball_light.png')
                self.set_properites()
                mouse_pos = pygame.mouse.get_pos()
                self.set_position(mouse_pos[0], mouse_pos[1])
                surf.blit(self.image, self.rect)
            elif self.highlight:
                self.image = pygame.image.load('ball_light.png')
                surf.blit(self.image, self.rect)
        else:
            self.height = 0
            self.weight = 0

    def set_properites(self):
        self.rect = self.image.get_rect()

        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery
        
    
    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y
        
class Box(Sprite):
    def __init__(self, createX, createY, dimX=100, dimY=100):
        Sprite.__init__(self)   
        self.rect = pygame.Rect(createX, createY, dimX, dimY)
        self.status = False
        
    def draw(self, surf, ball_list):
        self.highlight = self.rect.collidepoint(pygame.mouse.get_pos())
        for x in ball_list:
            if x.highlight:
                ball = x
                doNothing = False
            else:
                doNothing = True
        if not self.status:
            if not self.highlight:
                self.image = pygame.image.load('box.png')
                surf.blit(self.image, self.rect)
            if not doNothing:
                if self.rect.colliderect(ball.rect) and pygame.mouse.get_pressed()[0]:
                    self.image = pygame.image.load('box_ball_light.png')
                    surf.blit(self.image, self.rect)
                elif self.rect.colliderect(ball.rect) and not pygame.mouse.get_pressed()[0]:
                    self.image = pygame.image.load('boxball.png')
                    surf.blit(self.image, self.rect)
                    self.status = True
        else:
            self.image = pygame.image.load('boxball.png')
            surf.blit(self.image, self.rect)
            ball.status = True
    
HORIZ=800
VERT=600

my_clock = pygame.time.Clock()

my_screen = pygame.display.set_mode((HORIZ, VERT), 0, 32)
pygame.display.set_caption('Balls And Boxes')

WHITE = (255, 255, 255)
my_screen.fill(WHITE)

ball_list = [0 for i in range(3)]

ball_list[0] = Ball(200, 175)
ball_list[1] = Ball(400, 175)
ball_list[2] = Ball(600, 175)

box_list = [0 for i in range(3)]

box_list[0] = Box(200, 475)
box_list[1] = Box(400, 475)
box_list[2] = Box(600, 475)

pygame.display.update()

while True:
    for ev in pygame.event.get():    
        if ev.type == QUIT:
            pygame.quit()                
            sys.exit()
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:   
                pygame.quit()    
                sys.exit()    

    ball_list[0].draw(my_screen)
    ball_list[1].draw(my_screen)
    ball_list[2].draw(my_screen)
    
    box_list[0].draw(my_screen, ball_list)
    box_list[1].draw(my_screen, ball_list)
    box_list[2].draw(my_screen, ball_list)
    
    pygame.display.update()

    my_screen.fill(WHITE)
    
    my_clock.tick(50)
