import pygame


def runningcheck(event):
    if event.type == pygame.QUIT:
        return False
    elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
        return False
    else :
        return True
    
def mouseEvent(event, vals, grid):
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        mouse_x = (int(pos[0] / vals.GRID_SIZE))
        mouse_y = (int(pos[1] / vals.GRID_SIZE))
        grid.markCells((mouse_x, mouse_y))