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
        self.running = False

    def initArr(self):
        self.arr = [random.randrange(10,45)*10 for x in range(60)]
        self.clr2 = [(random.randrange(100,255), random.randrange(100,255), random.randrange(100,255)) for i in range(60)]
        self.clr = [(random.randrange(115,245), random.randrange(125,245), random.randrange(115,255))] * 60
        self.arrX = [(x+1)*8 for x in range(60)]

    def draw(self, x, y, clr):
        comb = zip(x, y, clr)
        for x, y, c in comb:
            pygame.draw.line(self.display_surface, c, (x, self.height), (x, self.height - y), 3)

    def update(self, time):
        pygame.time.delay(time)
        pygame.display.update()

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
                self.update(30)
        self.display_surface.fill((0,0,0))
        self.draw(self.arrX, self.arr, self.clr)
        self.update(30)

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
                pygame.draw.line(self.display_surface, (255, 0, 0), (self.arrX[currID], self.height), (self.arrX[currID], self.height - self.arr[currID]), 3)
                pygame.draw.line(self.display_surface, (255, 255, 255), (self.arrX[j], self.height), (self.arrX[j], self.height - self.arr[j]), 3)
                self.update(30)
            self.arr[currID], self.arr[i] = self.arr[i], curr
            self.clr[i] = (255, 0, 0)
        self.display_surface.fill((0,0,0))
        self.draw(self.arrX, self.arr, self.clr)
        self.update(30)

    def mergeSort(self, arr, lbound, rbound):
        mid = (lbound + rbound)//2
        self.check()
        if lbound < rbound:
            self.mergeSort(arr, lbound, mid)
            self.mergeSort(arr, mid+1, rbound)
            self.merge(arr, lbound, mid, mid+1, rbound)

    def merge(self, arr, lStart, lEnd, rStart, rEnd):
        self.check()
        i, j = lStart, rStart
        res = []
        while i <= lEnd and j <= rEnd:
            if arr[i] < arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
        while i <= lEnd:
            res.append(arr[i])
            i += 1
        while j <= rEnd:
            res.append(arr[j])
            j += 1
        j = 0
        for i in range(lStart, rEnd+1):
            self.arr[i] = res[j]
            j += 1
        self.display_surface.fill((0,0,0))
        self.draw(self.arrX, self.arr, self.clr)
        self.update(100)

    def cocktailSort(self):
        n = 0
        m = len(self.arr)
        while (n < m):
            self.check()
            for i in range(n, m - 1):
                if (self.arr[i] > self.arr[i+1]):
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    self.display_surface.fill((0,0,0))
                    self.draw(self.arrX, self.arr, self.clr)
                    pygame.draw.line(self.display_surface, (255, 255, 255), (self.arrX[i+1], self.height), (self.arrX[i+1], self.height - self.arr[i+1]), 3)
                    self.update(20)
            m -= 1
            for i in range(m - 1, n - 1, -1):
                if (self.arr[i] > self.arr[i+1]):
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    self.display_surface.fill((0,0,0))
                    self.draw(self.arrX, self.arr, self.clr)
                    pygame.draw.line(self.display_surface, (255, 255, 255), (self.arrX[i+1], self.height), (self.arrX[i+1], self.height - self.arr[i+1]), 3)
                    self.update(20)
            n += 1
        self.display_surface.fill((0,0,0))
        self.draw(self.arrX, self.arr, self.clr)
        self.update(20)


    def gnomeSort(self):
        i = 1
        while(i < len(self.arr)):
            self.check()
            if (self.arr[i-1] <= self.arr[i]):
                i += 1
            else:
                self.arr[i-1], self.arr[i] = self.arr[i], self.arr[i-1]
                self.display_surface.fill((0,0,0))
                self.draw(self.arrX, self.arr, self.clr)
                pygame.draw.line(self.display_surface, (255, 255, 255), (self.arrX[i], self.height), (self.arrX[i], self.height - self.arr[i]), 3)
                self.update(20)
                if (i > 1): i -= 1
        self.display_surface.fill((0,0,0))
        self.draw(self.arrX, self.arr, self.clr)
        self.update(20)

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
            elif keys[pygame.K_m]:
                self.mergeSort(self.arr, 0, len(self.arr)-1)
            elif keys[pygame.K_c]:
                self.cocktailSort()
            elif keys[pygame.K_g]:
                self.gnomeSort()
            elif keys[pygame.K_q]:
                pygame.quit()
                quit()
            self.clock.tick(15)

        pygame.quit()


s = Sort()
s.game()
