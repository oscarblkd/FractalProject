import numpy as np
import time as time
import pygame, os
from math import *
from numba import *
import scipy


os.environ["SDL_VIDEO_CENTERED"] = '1'  #for the fullscreen window

WIDTH, HEIGHT = 1920 , 1080 
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)

#Palette initialisation

colors = [(0, 0, 0)] + [(i, i, i) for i in range(256)]
palette = [pygame.Color(*color) for color in colors]

#Color Constant

BLUE = (13, 67, 216)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Complex Constant

C_JULIA_ONE = complex(0.285, 0.01)
C_JULIA_TWO = complex(-0.8, 0.156)
ZERO = complex(0, 0)

def main():
    
    pygame.init()
    run = True
    
    #Initialisation of the surface 
    
    image = supersample(C_JULIA_TWO, 2048, 4)
    image = image * 2
    surface = pygame.surfarray.make_surface(image)
    surface.set_palette(palette)
    screen.blit(surface, (0, 0))
    
    #Main loop
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
                
    pygame.quit()

@jit
def Julia_GPU(c = complex):
    
    """Return an array of the image data"""
    
    #Axis initialisation
    
    MAX_ITERATIONS = 2048
    image = np.empty((WIDTH, HEIGHT), dtype=np.int32)
    real_min = -2
    real_max = 2
    imaginary_min = -1
    imaginary_max = 1
    
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

@jit                
def smooth_coloring(c, max_iterations):
    """Return an array of the image data using the smooth coloring algorithm."""
    # Initialize the image array and the axis limits
    image = np.empty((WIDTH, HEIGHT), dtype=np.float32)
    real_min = -2
    real_max = 2
    imaginary_min = -1
    imaginary_max = 1

    # Iterate over each pixel in the image
    for x in range(WIDTH):
        for y in range(HEIGHT):
            iterations = 0
            z = complex(real_min + (real_max - real_min) * x / WIDTH, 
                        imaginary_min + (imaginary_max - imaginary_min) * y / HEIGHT)
            
            # Calculate the number of iterations until the point escapes to infinity
            while(iterations < max_iterations) and abs(z) < 4:
                iterations += 1
                z = z * z + c

            # Use the number of iterations to calculate the color of the pixel
            if iterations == max_iterations:
                image[x, y] = 0
            else:
                image[x, y] = iterations + 1 - log(log(abs(z)))/log(2)
    
    return image

@jit
def supersample(c, max_iterations, scale):
    """Return an array of the image data using supersampling."""
    # Initialize the image array and the axis limits
    image = np.empty((WIDTH * scale, HEIGHT * scale), dtype=np.float32)
    real_min = -2
    real_max = 2
    imaginary_min = -1
    imaginary_max = 1

    # Iterate over each pixel in the image
    for x in range(WIDTH * scale):
        for y in range(HEIGHT * scale):
            iterations = 0
            z = complex(real_min + (real_max - real_min) * x / (WIDTH * scale), 
                        imaginary_min + (imaginary_max - imaginary_min) * y / (HEIGHT * scale))
            
            # Calculate the number of iterations until the point escapes to infinity
            while(iterations < max_iterations) and abs(z) < 4:
                iterations += 1
                z = z * z + c

            # Use the number of iterations to calculate the color of the pixel
            if iterations == max_iterations:
                image[x, y] = 0
            else:
                image[x, y] = iterations + 1 - log(log(abs(z)))/log(2)
    
    # Scale the image down to the desired size
    image = scipy.ndimage.zoom(image, (WIDTH / image.shape[0], HEIGHT / image.shape[1]), order=1)
    
    return image
if __name__ == "__main__":
    main()
