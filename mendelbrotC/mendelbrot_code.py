import pygame
import numpy as np
from mendelbrot import mendelbrot_point

running = True

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_CENTER_X = int(WINDOW_WIDTH/2)
WINDOW_CENTER_Y = int(WINDOW_HEIGHT/2)

LIMITLOOP = 100
OUTLIMIT = 500

colors = [(i*3 % 256, i*5 % 256, i*7 % 256) for i in range(LIMITLOOP)]

def color_from_iter(iter):
    if iter < len(colors): return colors[iter]
    else: return (0, 0, 0)

def axis_translation(X,Y): # passed XY as screen coordinates
    global RE,IM
    deltax = X - WINDOW_CENTER_X
    deltay = Y - WINDOW_CENTER_Y
    RE += deltax*scale_factor
    IM += deltay*scale_factor

def draw_mendelbrot():
    for x,re in enumerate(RE):
        for y,im in enumerate(IM):
            color = color_from_iter(mendelbrot_point(re,im,LIMITLOOP,OUTLIMIT))
            screen.set_at((x,y), color)
    pygame.display.update()

if __name__ == '__main__':
    RE = np.arange(WINDOW_WIDTH,dtype=np.float64)-WINDOW_CENTER_X
    IM = np.arange(WINDOW_HEIGHT,dtype=np.float64)-WINDOW_CENTER_Y

    scale_factor = 4/WINDOW_HEIGHT
    RE = RE*scale_factor
    IM = IM*scale_factor
    # SETUP SCREEN
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Mendelbrot Set')

    # DRAW MENDELBROT
    draw_mendelbrot()

    # MAIN LOOP
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exit
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                r,i = pygame.mouse.get_pos() # x,y in the window related to the screen
                axis_translation(r,i)
                draw_mendelbrot()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    end_center_x,end_center_y = RE[WINDOW_CENTER_X]/2,IM[WINDOW_CENTER_Y]/2
                    scale_factor /= 2
                    RE /= 2
                    IM /= 2
                    RE += end_center_x
                    IM += end_center_y
                    LIMITLOOP += 100
                    OUTLIMIT *= 2
                    colors = [(i*3 % 256, i*5 % 256, i*7 % 256) for i in range(LIMITLOOP)]
                    draw_mendelbrot()
                    
                if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    end_center_x,end_center_y = RE[WINDOW_CENTER_X],IM[WINDOW_CENTER_Y] # non è chiaro il come ma funziona e quindi va bene cosi
                    scale_factor *= 2
                    RE *= 2
                    IM *= 2
                    RE -= (end_center_x)
                    IM -= (end_center_y)
                    LIMITLOOP -= 100
                    OUTLIMIT /= 2
                    colors = [(i*3 % 256, i*5 % 256, i*7 % 256) for i in range(LIMITLOOP)]
                    draw_mendelbrot()