

class CellCheck:
    def __init__(self, vals, rules) -> None:
        self.vals = vals
        self.rules = rules
    def startStop(self):
        self.vals.GAME_RUNNING = not self.vals.GAME_RUNNING  

    def update(self, grid):
        new_grid = [ [0] * grid.cols for _ in range(grid.rows)]
        if self.vals.GAME_RUNNING:
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
                        if self.rules.updateAlive(count):
                            new_grid[i][j] = 1
                    else:
                        if self.rules.updateDead(count):
                            new_grid[i][j] = 1
            grid.grid = new_grid

if __name__ == "__main__":
    print(f'Please open Programm wiht ../main.py.')
