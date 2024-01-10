import pygame

from modules.variable import *
from modules.grid import *
from modules.inputs import *
from modules.cellckecking import *

def game(): 
    pygame.init()
    vals = Settings()
    check = cellckecking()
    screen = pygame.display.set_mode(vals.WINDOW_SIZE)
    grid = Grid(screen, vals)
    inputs = Inputs(vals, grid, check)
    clock = pygame.time.Clock()
    
    # Loop
    count = 0
    while vals.WINDOW_OPEN:
        clock.tick(vals.FPS)
        screen.fill(vals.FIELD_BACKGROUND)
        if count > vals.FPS // vals.GAME_SPEED:
            check.update(grid)
            count = 0
        else: 
            count += 1
        grid.draw()
        pygame.display.update()
           
        
        #Key interaction
        #for event in pygame.event.get():
        #    running = inputs.runningcheck(event)
        #    inputs.mouseEvent(grid)
        #    inputs.inputs(event, check)
        inputs.update()   
            
    pygame.quit()  
    
    
if __name__ == "__main__":
    print(f"Programm only start with main.py")
