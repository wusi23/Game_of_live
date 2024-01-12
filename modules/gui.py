import pygame


class Gui:
    def __init__(self, vals, screen):
        self.vals = vals
        self.screen = screen
        self.fontFamily = "freesansbold.ttf"

    def draw(self):
        self.drawText(640, 15, self.gameRunningText(), 16, self.vals.FONTCOLOR_A, self.gameRunningTextBackground())
        #self.drawText(655, 50, " Start ", 32, self.vals.FONTCOLOR_A, self.vals.BUTTON_BACKGROUND)


    def drawText(self, pos_x, pos_y, text, text_size, fontcolor, fontbackground):
        font = pygame.font.Font(self.fontFamily, text_size)
        text = font.render(text, True, fontcolor, fontbackground)
        textRect = text.get_rect()
        textRect = (pos_x, pos_y)
        self.screen.blit(text, textRect)

    def gameRunningText(self):
        if self.vals.GAME_RUNNING:
            return "Game is running"
        else:
            return "Game is paused"

    def gameRunningTextBackground(self):
        if self.vals.GAME_RUNNING:
            return self.vals.GAME_RUNNING_BACKGROUND_RUN
        else:
            return self.vals.GAME_RUNNING_BACKGROUND_STOP
