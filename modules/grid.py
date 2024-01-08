import pygame


#own object for cells 
class ColsRows:
    def __init__(self, col, row, status = 0):
        self.col = col
        self.row = row
        self.status = status



class Grid:
    def __init__(self, screen, vals):
        self.screen = screen
        self.vals = vals
        self.cols = int(self.vals.WINDOW_SIZE[0] / self.vals.GRID_SIZE)
        self.rows = int(self.vals.WINDOW_SIZE[1] / self.vals.GRID_SIZE)
        self.grid = []
        self.make_Grid()
    
    def make_Grid(self):
        for i in range(self.cols):
            for j in range(self.rows):
               self.grid.append(ColsRows(i, j)) 
        
    def draw(self):
        for cel in self.grid:
            # Grid drawing
            pygame.draw.line(self.screen, self.vals.GRID_COLOR, (cel.col * self.vals.GRID_SIZE, cel.row * self.vals.GRID_SIZE), (cel.col * self.vals.GRID_SIZE + self.vals.GRID_SIZE, cel.row * self.vals.GRID_SIZE))
            pygame.draw.line(self.screen, self.vals.GRID_COLOR, (cel.col * self.vals.GRID_SIZE, cel.row * self.vals.GRID_SIZE), (cel.col * self.vals.GRID_SIZE, cel.row * self.vals.GRID_SIZE + self.vals.GRID_SIZE))
            
            # drawing the missing lines on the end of this grid
            pygame.draw.line(self.screen, self.vals.GRID_COLOR, (self.vals.WINDOW_SIZE[0] - 1, 0), (self.vals.WINDOW_SIZE[0] - 1, self.vals.WINDOW_SIZE[1]))
            pygame.draw.line(self.screen, self.vals.GRID_COLOR, (0, self.vals.WINDOW_SIZE[1] - 1), (self.vals.WINDOW_SIZE[0], self.vals.WINDOW_SIZE[1] - 1))
            
            # if cell alive color drawing
            if cel.status == 1:
                pygame.draw.rect(self.screen, self.vals.CELL_COLOR_ALIVE, (cel.col * self.vals.GRID_SIZE, cel.row * self.vals.GRID_SIZE ,self.vals.GRID_SIZE - 1, self.vals.GRID_SIZE - 1))
            # if cell dead color drawing    
            if cel.status == 2:
                pygame.draw.rect(self.screen, self.vals.CELL_COLOR_DEAD, (cel.col * self.vals.GRID_SIZE, cel.row * self.vals.GRID_SIZE ,self.vals.GRID_SIZE - 1, self.vals.GRID_SIZE - 1))
                
    def markCells(self, mousePos):
        for cel in self.grid:
            # if var mousePos not korrekt protection
            if mousePos == None:
                continue
            else:
                if cel.col == mousePos[0] and cel.row == mousePos[1]: 
                    cel.status = 1
                
                         
                
                
if __name__ == "__main__":
    print(f"Programm only start with main.py")                