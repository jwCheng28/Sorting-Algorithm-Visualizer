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
        #self.arr = [random.randrange(10,45)*10 for x in range(30)]
        #self.clr = [(random.randrange(100,255), random.randrange(100,255), random.randrange(100,255)) for i in range(30)]
        #self.arrX = [(x+1)*15 for x in range(30)]
        self.running = False

    def initArr(self):
        self.arr = [random.randrange(10,45)*10 for x in range(30)]
        self.clr = [(random.randrange(100,255), random.randrange(100,255), random.randrange(100,255)) for i in range(30)]
        self.arrX = [(x+1)*15 for x in range(30)]

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
                pygame.draw.line(self.display_surface, (255, 255, 255), (self.arrX[j+1], self.height), (self.arrX[j+1], self.height - self.arr[j+1]), 3)
                pygame.time.delay(30)
                pygame.display.update()
        self.running = False

    def selectionSort(self):
        for i in range(len(self.arr)):
            curr, currID = self.arr[i], i
            for j in range(i+1, len(self.arr)):
                self.check()
                temp = self.arr[j]
                if temp < curr:
                    curr, currID = temp, j
                self.display_surface.fill((0,0,0))
                self.draw(self.arrX, self.arr, self.clr)
                pygame.draw.line(self.display_surface, (255, 255, 255), (self.arrX[j], self.height), (self.arrX[j], self.height - self.arr[j]), 3)
                pygame.time.delay(30)
                pygame.display.update()
            self.arr[currID], self.arr[i] = self.arr[i], curr
        self.running = False

    def game(self):
        self.initArr()
        count = 0
        while True:
            keys = pygame.key.get_pressed()
            self.check()
            if keys[pygame.K_SPACE]:
                count = 1
                self.initArr()
                self.running = True
                self.display_surface.fill((0,0,0))
                self.draw(self.arrX, self.arr, self.clr)
                pygame.display.update()

            if self.running == False:
                self.display_surface.fill((0,0,0))
                if count != 0:
                    self.draw(self.arrX, self.arr, self.clr)
                pygame.display.update()

            elif keys[pygame.K_s]:
                self.selectionSort()
            elif keys[pygame.K_b]:
                self.bubbleSort()
            elif keys[pygame.K_q]:
                pygame.quit()
                quit()
            self.clock.tick(20)

        pygame.quit()


s = Sort()
s.game()
