import pygame
import random

class Display:
    def __init__(self, width, height, barHeightRange, barColorRange, barAmount, display_surface):
        self.width = width
        self.height = height
        self.heightRange = barHeightRange
        self.colorRange = barColorRange
        self.barAmount = barAmount
        self.display_surface = display_surface

    def createBars(self):
        self.barLoc = [i*8 for i in range(1, self.barAmount+1)]
        self.barH = [random.randrange(*self.heightRange)*10 for i in range(self.barAmount)]
        self.barCLR = [
            random.randrange(*self.colorRange),
            random.randrange(*self.colorRange),
            random.randrange(*self.colorRange)
        ] * self.barAmount

    def drawBars(self, xLocs=None, yLocs=None, colors=None):
        if not xLocs and not yLocs and not colors:
            xLocs, yLocs, colors = self.barLoc, self.barH, self.barCLR

        for x, y, c in zip(xLocs, yLocs, colors):
            pygame.draw.line(
                self.display_surface, c,
                (x, self.height), (x, self.height - y), 3
            )

    def recolorIndex(self, index, color=(255,255,255)):
        pygame.draw.line(
            self.display_surface, color,
            (self.barLoc[index], self.height),
            (self.barLoc[index], self.height - self.barH[index]), 3
        )

    def update(self, timeDelay):
        pygame.time.delay(timeDelay)
        pygame.display.update()

    def checkQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
