
import numpy as np
import pygame, os
from Complex import *
from numba import jit, njit, vectorize, cuda, uint32, f8, uint8

os.environ["SDL_VIDEO_CENTERED"] = '1'  #for the fullscreen window

WIDTH, HEIGHT = 1920, 1080
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)

BLUE = (13, 67, 216)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

C_JULIA_ONE = Complex(0.285, 0.01)
C_JULIA_TWO = Complex(-0.8, 0.156)
ZERO = Complex(0, 0)




def main():
    run = True
    screen.fill(WHITE)
    Julia(C_JULIA_ONE)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
                
    pygame.quit()

def Julia(c = Complex):
    
    MAX_ITERATIONS = 5000
    
    real_min = -2
    real_max = 2
    imaginary_min = -2
    imaginary_max = 2
    
    #Sequence of z(n + 1) = z(n)² + C where C is a constant 
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            iterations = 0
            z = Complex(real_min + (real_max - real_min) * x / WIDTH, 
                        imaginary_min + (imaginary_max - imaginary_min) * y / HEIGHT)
            
            while(iterations < MAX_ITERATIONS) and Complex.abs(z) < 4:
                iterations += 1
                z = (z.product(z)).sum(c)
                
            #Color gestion 

            color = int((16 * iterations / 100) % 255), int((16 * iterations / 100) % 255), int((128 * iterations / 100) % 255)
            screen.set_at((x, y), color)

if __name__ == "__main__":
    main()
