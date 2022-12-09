import numpy as np
import pygame, os, complex



#SETUP
os.environ["SDL_VIDEO_CENTERED"] = '1'  #for the fullscreen window
WIDTH, HEIGHT = 1920, 1080
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)
BLUE = (13, 67, 216)

#Objet complexe
class Complex():

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def sum(self, unComplexe):
        return self.real + unComplexe.real, self.imaginary + unComplexe.imaginary

    

def main():
    run = True
    screen.fill(BLUE)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
                
    pygame.quit()


