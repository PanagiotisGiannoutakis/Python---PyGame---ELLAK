import pygame

class Main_Frame(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load('bg_green.png')
        
