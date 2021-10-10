import pygame
from pygame.locals import *

## Διαστάσεις παραθύρου
HEIGHT = 800
WIDTH = 600

## Βασικά χρώματα στην κλίμακα RGB
RED = (255, 0 , 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0 , 255)
GREEN = (0, 255, 0)

if (__name__== "__main__"):
    

    pygame.init()

    my_window = pygame.display.set_mode((HEIGHT, WIDTH))
    
    pic = pygame.image.load('bg_green.png')

    my_window.

    my_window.fill(WHITE)

    pygame.display.update()
