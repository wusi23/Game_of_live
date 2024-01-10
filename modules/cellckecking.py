

class cellckecking:
    def __init__(self) -> None:
        self.running = False
   
    def startStop(self):
           self.running = not self.running

    def update(self, grid):
        new_grid = [ [0] * grid.cols for _ in range(grid.rows)]
        if self.running:
            # i is col 
            # j is row
            for i in range(len(grid.grid)):
                for j in range(len(grid.grid[i])):
                    count = 0
                    if i + 1 >= len(grid.grid):
                        pass
                    else:
                        if j + 1 >= len(grid.grid[i]):
                            pass
                        else:
                            #right
                            if grid.grid[i + 1][j]:
                                count += 1
                            #right bottom
                            if grid.grid[i + 1][j + 1]:
                                count += 1
                            #right top
                            if grid.grid[i + 1][j - 1]:
                                count += 1
                            #left
                            if grid.grid[i - 1][j]:
                                count += 1
                            #left bottom
                            if grid.grid[i - 1][j + 1]:
                                count += 1
                            #left top
                            if grid.grid[i - 1][j - 1]:
                                count += 1
                            #top
                            if grid.grid[i][j - 1]:
                                count += 1
                            #bottom
                            if grid.grid[i][j + 1]:
                                count += 1
                    if grid.grid[i][j]:
                        if count == 2 or count == 3:
                            new_grid[i][j] = 1
                    else:
                        if count == 3:
                            new_grid[i][j] = 1
            grid.grid = new_grid

if __name__ == "__main__":
    print(f'Please open Programm wiht ../main.py.')
