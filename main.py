import time
import pygame
import numpy as np


COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
#COLOR_DIE_NEXT = (170, 170, 170)
COLOR_DIE_NEXT = (0, 0, 0)
COLOR_ALIVE_NEXT = (255, 255, 255)

CELL_SIZE = 30
WINDOW_X = 1080 
WINDOW_Y = 780
GAME_SPEED = 0.1


def update(screen, cells, size, with_progress=False):
    update_cells = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <=3:
                update_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT         
        else:
            if alive == 3:
                update_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    return update_cells

def main(GAME_SPEED):
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    
    cells = np.zeros((int(WINDOW_Y / CELL_SIZE), int(WINDOW_X / CELL_SIZE)))
    screen.fill(COLOR_GRID)
    
    update(screen, cells, CELL_SIZE)
    
    pygame.display.flip()
    pygame.display.update()
    
    running = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    GAME_SPEED = GAME_SPEED + 0.1
                if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    if GAME_SPEED < 0.0001:
                        GAME_SPEED = 0.0001
                    else:
                        GAME_SPEED = GAME_SPEED - 0.1
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    GAME_SPEED = 0.1
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, CELL_SIZE)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // CELL_SIZE, pos[0] // CELL_SIZE] = 1
                update(screen, cells, CELL_SIZE)
                pygame.display.update()
        screen.fill(COLOR_GRID)
            
        if running:
            cells = update(screen, cells, CELL_SIZE, with_progress=True)
            pygame.display.update()
            time.sleep(GAME_SPEED)
            
if __name__ == '__main__':
    main(GAME_SPEED)
    