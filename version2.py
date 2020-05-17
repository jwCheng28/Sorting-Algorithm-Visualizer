import pygame
import random

class Sort:

    WIDTH = 500
    HEIGHT = 500
    WHITE = (255, 255, 255)

    def __init__(self, width = WIDTH, height = HEIGHT):
        pygame.init()
        self.width = width
        self.height = height
        self.display_surface = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Algorithm Visualizer')

        pygame.display.update()
        self.arr = [random.randrange(10,45)*10 for x in range(30)]
        self.clr = [(random.randrange(100,255), random.randrange(100,255), random.randrange(100,255)) for i in range(30)]
        self.arrX = [(x+1)*15 for x in range(30)]
        self.running = False

    def draw(self, x, y, clr):
        comb = zip(x, y, clr)
        for x, y, c in comb:
            pygame.draw.line(self.display_surface, c, (x, self.height), (x, self.height - y), 3)

    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def bubbleSort(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)-i-1):
                self.check()
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1],self.arr[j]
                    self.clr[j], self.clr[j+1] = self.clr[j+1], self.clr[j]
                self.display_surface.fill((0,0,0))
                self.draw(self.arrX, self.arr, self.clr)
                pygame.time.delay(60)
                pygame.display.update()
        self.running = False

    def game(self):
        while True:
            keys = pygame.key.get_pressed() 
            self.check()
            if keys[pygame.K_SPACE]:
                self.running = True

            if self.running == False:
                self.display_surface.fill((0,0,0))
                self.draw(self.arrX, self.arr, self.clr)
                pygame.display.update()

            else:
                self.bubbleSort()

            self.clock.tick(20)

        pygame.quit()


s = Sort()
s.game()