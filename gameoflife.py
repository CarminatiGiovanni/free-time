import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
BLOCKSIZE = 10 #Set the size of the grid block
TICKSPEED = 100 #Set the speed of the game
X = int(WINDOW_WIDTH / BLOCKSIZE)
Y = int(WINDOW_HEIGHT / BLOCKSIZE)

running = True
start = False

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

game_grid = [[0 for _ in range(X)] for _ in range(Y)]
new_grid = [[0 for _ in range(X)] for _ in range(Y)]

oldcol,oldrow = 0,0

def color_from_age(age):
    if age == 0:
        return BLACK
    elif age == 1:
        return (255, 0, 0)  # Red
    elif age == 2:
        return (255, 165, 0)  # Orange
    elif age == 3:
        return (255, 255, 0)  # Yellow
    elif age == 4:
        return (0, 255, 0)  # Green
    elif age == 5:
        return (0, 255, 255)  # Cyan
    elif age == 6:
        return (0, 0, 255)  # Blue
    elif age == 7:
        return (75, 0, 130)  # Indigo
    elif age == 8:
        return (238, 130, 238)  # Violet
    elif age == 9:
        return (255, 255, 255)  # White
    else:
        return (128, 0, 128)  # Purple

def count_neiboors(x, y):
    count = 0
    if game_grid[y-1][x] != 0: count += 1
    if game_grid[y-1][x-1] != 0: count += 1
    if game_grid[y-1][(x+1)%X] != 0: count += 1
    if game_grid[(y+1)%Y][x-1] != 0: count += 1
    if game_grid[(y+1)%Y][x] != 0: count += 1
    if game_grid[(y+1)%Y][(x+1)%X] != 0: count += 1
    if game_grid[y][x-1] != 0: count += 1
    if game_grid[y][(x+1)%X] != 0: count += 1
    return count

def calculate_new_grid():
    # print('-------------------------------------------------------------------------')
    new_grid = [[0 for _ in range(X)] for _ in range(Y)]
    for y in range(Y):
        for x in range(X):
            neiboors = count_neiboors(x, y)
            if neiboors < 2 or neiboors > 3: # die due overpopulation or underpopulation
                new_grid[y][x] = 0
            elif neiboors == 2 and game_grid[y][x] != 0: # stay alive
                new_grid[y][x] = game_grid[y][x] + 1
            elif neiboors == 3 and game_grid[y][x] == 0: # born
                new_grid[y][x] = 1
            elif neiboors == 3 and game_grid[y][x] != 0: # stay alive
                new_grid[y][x] = game_grid[y][x] + 1
            else: # 2 neiboors but dead
                new_grid[y][x] = 0
    
    return new_grid.copy()

def drawGrid():
    for y in range(Y):
        for x in range(X):
            rect = pygame.Rect(x * BLOCKSIZE, y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, color_from_age(game_grid[y][x]), rect, 0)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Game of Life')
    drawGrid()
    pygame.display.update()
    while running:
        if start == True:
            pygame.time.delay(TICKSPEED)
            game_grid = calculate_new_grid()
            drawGrid()
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if (not start) and event.button == 1:
            #         row = int(event.pos[1] // BLOCKSIZE)
            #         col = int(event.pos[0] // BLOCKSIZE)
            #         game_grid[row][col] = (game_grid[row][col] + 1)%2
            #         drawGrid()
            #         pygame.display.update()

            if event.type == pygame.KEYDOWN:
                start = not start

        if start == False:
            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if click[0] == True:
                row = int(cur[1] // BLOCKSIZE)
                col = int(cur[0] // BLOCKSIZE)
                if (row,col) != (oldrow,oldcol) and row < Y and col < X:
                    game_grid[row][col] = 0 if game_grid[row][col] != 0 else 1
                    drawGrid()
                    pygame.display.update()
                oldrow = row
                oldcol = col
    pygame.quit()