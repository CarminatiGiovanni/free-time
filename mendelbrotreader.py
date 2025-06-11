import pygame
import pandas as pd
import numpy as np
import os
import subprocess

# Define the path to your .exe file and the arguments
exe_path = "C:\\Users\\jocar\\Desktop\\orbit\\mendelbrot.exe"

# Run the .exe file with the specified arguments

import time

running = True

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

LIMITLOOP = 100
OUTLIMIT = 500

rmin,rmax,imin,imax = -2.2,+0.8,-1.5,+1.5
rcenter,icenter = (rmin + rmax)/2, (imin + imax)/2

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Mendelbrot Set')

def drawpxel(x, y, color):
    screen.set_at((x,y), color)

colors = [(i*2 % 256, i*5 % 256, i*7 % 256) for i in range(LIMITLOOP)]

def color_from_iter(iter):
    if iter < len(colors):
        return colors[iter]
    else:
        return (0, 0, 0)

def draw_mendelbrot(rmin,rmax,imin,imax):
    command = f"{exe_path} {WINDOW_WIDTH} {WINDOW_HEIGHT} {rmin} {rmax} {imin} {imax} {LIMITLOOP}"
    print(command)
    subprocess.run(command)
    time.sleep(1)
    df = pd.read_csv('mendelbrot.txt',sep=' ', header=None).to_numpy(dtype=np.int16)
    for i in range(0,WINDOW_HEIGHT):
        for j in range(0,WINDOW_WIDTH):
            color = color_from_iter(df[i][j])
            # print(iter)
            drawpxel(j,i,color)

draw_mendelbrot(rmin,rmax,imin,imax)
pygame.display.update()

while running:
    #print(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            r,i = pygame.mouse.get_pos()
            print('x:',r,'y:',i)
            r = rmin + ((rmax - rmin)/WINDOW_WIDTH) *r
            i = imax - ((imax - imin)/WINDOW_HEIGHT) *i
            deltar = -(rcenter - r)
            rmin += deltar
            rmax += deltar
            deltai = -(icenter - i) 
            imin += deltai
            imax += deltai
            rcenter,icenter = (rmin + rmax)/2, (imin + imax)/2
            if pygame.mouse.get_pressed()[0]: # zoom in
                rmin *= 0.5
                rmax *= 0.5
                imin *= 0.5
                imax *= 0.5
                rcenter *= 0.5
                icenter *= 0.5
                LIMITLOOP = int(LIMITLOOP*1.5)
            else: # zoom out
                rmin *= 1.5
                rmax *= 1.5
                imin *= 1.5
                imax *= 1.5
                rcenter *= 1.5
                icenter *= 1.5
                LIMITLOOP = int(LIMITLOOP*0.5)

            draw_mendelbrot(rmin,rmax,imin,imax)
            pygame.display.update()