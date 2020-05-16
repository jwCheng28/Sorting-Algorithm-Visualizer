import pygame
import random

pygame.init()
width = 500
height = 500
WHITE = (255, 255, 255)
display_surface = pygame.display.set_mode((width, height))
pygame.display.update()
pygame.display.set_caption('Pygame')
clock = pygame.time.Clock()
crashed = False

arr = [random.randrange(10,45)*10 for x in range(30)]
clr = x = [(random.randrange(100,255), random.randrange(100,255), random.randrange(100,255)) for i in range(30)]
arrX = [(x+1)*15 for x in range(30)]
j = 0

def draw(x, y, clr):
    pygame.draw.line(display_surface, clr, (x, height), (x, height - y), 3)

while not crashed:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    comb = zip(arr, clr, arrX)
    display_surface.fill((0,0,0))
    for y, c, x in comb:
        draw(x, y, c)
    pygame.time.delay(5)
    if arr[j] < arr[j+1]:
        arr[j], arr[j+1] = arr[j+1],arr[j]
        clr[j], clr[j+1] = clr[j+1], clr[j]
    if j < len(arr)-2:
        j += 1
    else:
        j = 0
 
    print(arr)
    pygame.display.update()
    clock.tick(20)

