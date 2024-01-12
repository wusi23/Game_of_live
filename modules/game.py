import pygame

from modules.variable import *
from modules.grid import *
from modules.inputs import *
from modules.cellckecking import *
from modules.gui import *
from modules.rules import *

def game(): 
    pygame.init()
    pygame.display.set_caption("Game of life")
    vals = Settings()
    rules = Rules(vals)
    check = CellCheck(vals, rules)
    screen = pygame.display.set_mode(vals.WINDOW_SIZE)
    gui = Gui(vals, screen)
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
        gui.draw()
        pygame.display.update()
        inputs.update()   
            
    pygame.quit()  
    
    
if __name__ == "__main__":
    print(f"Programm only start with main.py")
