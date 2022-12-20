import numpy as np
import pygame, os
from math import *
from numba import *



os.environ["SDL_VIDEO_CENTERED"] = '1'  #for the fullscreen window

WIDTH, HEIGHT = 1920 , 1080 
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)

#Palette initialisation

colors = [(0, 0, 0)] + [(0, 0, i) for i in range(256)]
black_to_blue = [pygame.Color(*color) for color in colors]

colors = [(0, 0, 0)] + [(i, 0, 0) for i in range(256)]
black_to_red = [pygame.Color(*color) for color in colors]

colors = [(0, 0, 0)] + [(0, i, 0) for i in range(256)]
black_to_green = [pygame.Color(*color) for color in colors]

#Color Constant

BLUE = (13, 67, 216)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Complex Constant

C_JULIA_ONE = complex(0.285, 0.01)
C_JULIA_TWO = complex( -1.476, 0)
C_JULIA_THREE = complex(0, 0.8)
C_JULIA_FOUR = complex(0.355 , 0.355)
C_JULIA_FIVE = complex(-0.4, -0.59)
ZERO = complex(0, 0)

def main():
    
    pygame.init()
    run = True
    
    #Initialisation of the surface 
    
    image = julia(C_JULIA_FIVE)
    image = image * 2
    surface = pygame.surfarray.make_surface(image)
    surface.set_palette(black_to_blue)
    screen.blit(surface, (0, 0))
    
    #Main loop
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
                
    pygame.quit()

@jit
def julia(c : complex):
    
    """Return an array of the image data"""
    
    #Axis initialisation
    
    MAX_ITERATIONS = 2048
    image = np.empty((WIDTH, HEIGHT), dtype=np.int32)
    real_min = -2
    real_max = 2
    imaginary_min = -1.5
    imaginary_max = 1.5
    
    #Sequence of z(n + 1) = z(n)² + C where C is a constant 
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            iterations = 0
            z = complex(real_min + (real_max - real_min) * x / WIDTH, 
                        imaginary_min + (imaginary_max - imaginary_min) * y / HEIGHT)
            
            while(iterations < MAX_ITERATIONS) and abs(z) < 4:
                iterations += 1
                z = z * z + c
            image[x, y] = iterations
    return image

if __name__ == "__main__":
    main()
