
class Settings:
    def __init__(self):
        self.GRID_COLOR = (50, 50, 50)
        self.GRID_SIZE = 10
        self.CELL_COLOR_ALIVE = (0, 255, 0)
        self.CELL_COLOR_DEAD =  (0, 0 ,0)
        self.FIELD_BACKGROUND = (150, 150, 150)
        self.FIELD_COLOR = (255, 255, 255)
        self.WINDOW_SIZE = (800, 800)
        self.FPS = 30
        self.INIT_SPEED = 10
        self.MAX_SPEED = 20
        self.GAME_SPEED = 10 
        self.WINDOW_OPEN = True


if __name__ == "__main__":
    print(f"Programm only start with main.py")
