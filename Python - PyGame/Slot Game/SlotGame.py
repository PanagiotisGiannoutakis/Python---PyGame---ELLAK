import pygame, sys, random
from pygame.locals import *

class Box():
    def __init__( self, imageURL, x, y, surface):
        self.image = pygame.image.load(imageURL)
        surface.blit(self.image, (x,y))

pygame.init()

## Διαστάσεις του παραθύρου
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

GLOBAL_SCORE = 0
MY_SOUND = pygame.mixer.Sound('Sound Slot Machine.wav')
    
def eventHandle(surface):
    
    for event in pygame.event.get():
        if event.type == QUIT:
            return True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return True
            if event.key == K_SPACE:
                MY_SOUND.stop()
                play_Game(surface)
    return False

def get_Score(table):

    score = 0
    
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2]:
            score += 1
        if table[0][i] == table[1][i] == table[2][i]:
            score += 2

    if table[0][0] == table[1][1] == table[2][2]:
        score += 3

    if table[0][2] == table[1][1] == table[2][0]:
        score += 4

    return score

def play_Game(my_window):

    global GLOBAL_SCORE, MY_SOUND

    MY_SOUND.play()
    
    background_image = pygame.image.load('background.png')
    my_window.blit(background_image, (0, 0))
        
    my_font = pygame.font.SysFont('Arial Black', 30)
    my_text = my_font.render('Your score is: ' + str(GLOBAL_SCORE), False, RED, BLUE)
    my_window.blit(my_text, ((background_image.get_width() - my_text.get_width())/2, (background_image.get_height() - my_text.get_height())/2 - 230))

    my_font = pygame.font.SysFont('Arial Black', 18)
    my_text = my_font.render('Πάτησε SPACE για να συνεχίσεις, ESCAPE για να φύγεις... ', False, RED, BLUE)
    my_window.blit(my_text, ((background_image.get_width() - my_text.get_width())/2, (background_image.get_height() - my_text.get_height())/2 + 230))

    pygame.display.update()
    
    for k in range(250):
        
        background_image1 = pygame.image.load('background1.png')
        my_window.blit(background_image1, (252, 152))
        
        table = [[random.randint(0,2) for i in range(3)] for j in range(3)]
        
        setX = 275
        setY = 175

        for i in range(3):

            if i == 0:
                setY = 175
            elif i == 1:
                setY = 275
            elif i == 2:
                setY = 375

            for j in range(3):

                if j == 0:
                    setX = 275
                elif j == 1:
                    setX = 375
                elif j == 2:
                    setX = 475
                
                if table[i][j] == 0:
                    new_box = Box('ubuntu.png', setX, setY, my_window)
                elif table[i][j] == 1:
                    new_box = Box('microsoft.png', setX, setY, my_window)
                elif table[i][j] == 2:
                    new_box = Box('apple.png', setX, setY, my_window)

        pygame.display.update()
        
    GLOBAL_SCORE += get_Score(table)

    my_font = pygame.font.SysFont('Arial Black', 30)
    my_text = my_font.render('Your score is: ' + str(GLOBAL_SCORE), False, RED, BLUE)
    my_window.blit(my_text, ((background_image.get_width() - my_text.get_width())/2, (background_image.get_height() - my_text.get_height())/2 - 230))

    pygame.display.update()
    
def main():
    dimensions = (HEIGHT, WIDTH)
    
    my_window = pygame.display.set_mode(dimensions)
    pygame.display.set_caption('Slot Game in Python')

    background_image = pygame.image.load('background.png')
    my_window.blit(background_image, (0, 0))

    my_font = pygame.font.SysFont('Arial Black', 45)
    my_text = my_font.render('Ας παίξουμε φρουτάκια !!!', False, RED, BLUE)
    my_text = pygame.transform.scale(my_text, (my_text.get_width(), my_text.get_height() + 10))
    my_window.blit(my_text, ((dimensions[0] - my_text.get_width()) / 2, ((dimensions[1] - my_text.get_height()) / 2) - 200))

    instructions = pygame.image.load('instructions.png')
    my_window.blit(instructions, ((dimensions[0]-instructions.get_width())/2, (dimensions[1]-instructions.get_height())/2))

    my_font = pygame.font.SysFont('Arial Black', 20)
    my_text = my_font.render('Πάτησε SPACE για να ξεκινήσεις...', False, RED, BLUE)
    my_text = pygame.transform.scale(my_text, (my_text.get_width(), my_text.get_height() + 10))
    my_window.blit(my_text, ((dimensions[0] - my_text.get_width()) / 2, ((dimensions[1] - my_text.get_height()) / 2) + 200))
    
    pygame.display.update()
    
    continueGame = False
    
    while not continueGame:
        continueGame = eventHandle(my_window)

    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    main()
