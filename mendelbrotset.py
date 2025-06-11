import pygame

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

colors = [(i*2 % 256, i*5 % 256, i*7 % 256) for i in range(100)]

def color_from_iter(iter):
    if iter < len(colors):
        return colors[iter]
    else:
        return (0, 0, 0)

def mendelpoint(c):
    z = 0 + 0j
    for iter in range(0,LIMITLOOP):
        z = z*z + c 
        if abs(z*z) > OUTLIMIT: return color_from_iter(iter), iter
    return (255,0,0), 20

def draw_mendelbrot(rmin,rmax,imin,imax):
    rstep = abs(rmax-rmin)/WINDOW_WIDTH
    istep = abs(imax-imin)/WINDOW_HEIGHT
    for i in range(0,WINDOW_WIDTH):
        for j in range(0,WINDOW_HEIGHT):
            c = complex(rmin + rstep*i,imin + istep*j)
            color,iter = mendelpoint(c)
            # print(iter)
            drawpxel(i,j,color)

draw_mendelbrot(rmin,rmax,imin,imax)
pygame.display.update()

while running:
    #print(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            r,i = pygame.mouse.get_pos()
            r = rmin + (rmax - rmin)*r/WINDOW_WIDTH
            i = imin + (imax - imin)*i/WINDOW_HEIGHT
            deltar = (rcenter + r)/2
            rmin += deltar
            rmax += deltar
            deltai = (icenter + i)/2 
            imin += deltai
            imax += deltai
            rcenter = r
            icenter = i
            if pygame.mouse.get_pressed()[0]: # zoom in
                rmin *= 0.5
                rmax *= 0.5
                imin *= 0.5
                imax *= 0.5
            else: # zoom out
                rmin *= 1.5
                rmax *= 1.5
                imin *= 1.5
                imax *= 1.5
            draw_mendelbrot(rmin,rmax,imin,imax)
            pygame.display.update()