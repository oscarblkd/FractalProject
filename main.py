
import numpy as np
import pygame, os
from Complex import *

os.environ["SDL_VIDEO_CENTERED"] = '1'  #for the fullscreen window

WIDTH, HEIGHT = 1920, 1080
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)

BLUE = (13, 67, 216)
WHITE = (255, 255, 255)

def main():
    run = True
    screen.fill(BLUE)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
                
    pygame.quit()

def Mandelbrot():

if __name__ == "__main__":
    main()
