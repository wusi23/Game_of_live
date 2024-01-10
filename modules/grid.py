import pygame


class Grid:
    def __init__(self, screen, vals):
        self.screen = screen
        self.vals = vals
        self.cols = int(self.vals.WINDOW_SIZE[0] / self.vals.GRID_SIZE)
        self.rows = int(self.vals.WINDOW_SIZE[1] / self.vals.GRID_SIZE)
        self.grid = [ [0] * self.cols for _ in range(self.rows)]
 
    def draw(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 1:
                    temp_Color = self.vals.CELL_COLOR_ALIVE
                else:
                    temp_Color = self.vals.CELL_COLOR_DEAD   
                pygame.draw.rect(
                    self.screen, 
                    temp_Color, 
                    ((i * self.vals.GRID_SIZE), 
                    j * self.vals.GRID_SIZE, 
                    self.vals.GRID_SIZE - 1, 
                    self.vals.GRID_SIZE - 1))

                
    def markCells(self, mousePos):
            # if nonsen from mousePos protection 
            if mousePos == None:
                pass
            else:
                self.grid[mousePos[0]][mousePos[1]] = 1 
                    
                
if __name__ == "__main__":
    print(f"Programm only start with main.py")                
