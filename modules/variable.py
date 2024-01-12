
class Settings:
    def __init__(self):
        self.GRID_COLOR = (50, 50, 50)
        self.GRID_SIZE = 20
        self.CELL_COLOR_ALIVE = (0, 255, 0)
        self.CELL_COLOR_DEAD =  (0, 0 ,0)
        self.FIELD_BACKGROUND = (10, 10, 10)
        self.FIELD_COLOR = (255, 255, 255)
        self.WINDOW_SIZE = (800, 800)
        self.GAME_SIZE = (800, self.WINDOW_SIZE[1] - 200)
        self.FPS = 30
        self.INIT_SPEED = 10
        self.MAX_SPEED = 20
        self.GAME_SPEED = 10 
        self.WINDOW_OPEN = True
        self.GAME_RUNNING = False
        # ruleset from 1 to 11
        self.RULE_SET = 3
        #GUI COLORS
        self.FONTCOLOR_A = (255, 255, 255)
        self.BUTTON_BACKGROUND = (100, 100, 100)
        self.GAME_RUNNING_BACKGROUND_RUN = (0, 255, 0)
        self.GAME_RUNNING_BACKGROUND_STOP = (255, 0, 0)


if __name__ == "__main__":
    print(f"Programm only start with main.py")
