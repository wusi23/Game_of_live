import pygame

class Inputs:
    def __init__(self, vals, grid, check):
        self.vals = vals
        self.grid = grid
        self.check = check


    def windowControlfield(self, event):
        if event.type == pygame.QUIT:
            self.vals.WINDOW_OPEN = False 
    
    def mouseEvents(self):
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            mouse_x = (int(pos[0] / self.vals.GRID_SIZE))
            mouse_y = (int(pos[1] / self.vals.GRID_SIZE))
            self.grid.markCells((mouse_x, mouse_y))
        
    def keyInputs(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.check.startStop()
            elif event.key == pygame.K_ESCAPE:
                self.vals.WINDOW_OPEN = False
            elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                if self.vals.GAME_SPEED < self.vals.MAX_SPEED:
                    self.vals.GAME_SPEED += 1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                if self.vals.GAME_SPEED - 1 != 0:
                    self.vals.GAME_SPEED -= 1
            elif event.key == pygame.K_0 or event.key == pygame.K_KP_0:
                self.vals.GAME_SPEED = self.vals.INIT_SPEED


    def update(self): 
        for event in pygame.event.get():
            self.windowControlfield(event)
            self.mouseEvents()
            self.keyInputs(event)


if __name__ == "__main__":
    print(f"Programm only start with main.py")
