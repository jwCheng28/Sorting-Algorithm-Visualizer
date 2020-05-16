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
        self.j = 0

    def draw(self, x, y, clr):
        pygame.draw.line(self.display_surface, clr, (x, self.height), (x, self.height - y), 3)
    
    def bubble(self):
        if self.arr[self.j] < self.arr[self.j+1]:
            self.arr[self.j], self.arr[self.j+1] = self.arr[self.j+1], self.arr[self.j]
            self.clr[self.j], self.clr[self.j+1] = self.clr[self.j+1], self.clr[self.j]
        if self.j < len(self.arr)-2:
            self.j += 1
        else:
            self.j = 0

    def display(self):
        comb = zip(self.arr, self.clr, self.arrX)
        self.display_surface.fill((0,0,0))
        for y, c, x in comb:
            self.draw(x, y, c)

    def game(self):
        while not False:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.display()
            self.bubble()
            print(self.arr)
            pygame.display.update()
            self.clock.tick(20)

g = Sort()
g.game()