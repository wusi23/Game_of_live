import pygame

from modules.variable import *
from modules.grid import *
from modules.interface import *

def game(): 
    pygame.init()
    vals = Settings()
    screen = pygame.display.set_mode(vals.WINDOW_SIZE)
    grid = Grid(screen, vals)
    clock = pygame.time.Clock()
    running = True
    

    while running:
        clock.tick(vals.FPS)
        screen.fill(vals.FIELD_BACKGROUND)
        grid.draw()
        pygame.display.update()
        
        #Key interaction
        for event in pygame.event.get():
            running = runningcheck(event)
            mouseEvent(event, vals, grid)
    pygame.quit()  
    
    
if __name__ == "__main__":
    print(f"Programm only start with main.py")