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
running = False


arr = [random.randrange(10,45)*10 for x in range(30)]
clr = x = [(random.randrange(100,255), random.randrange(100,255), random.randrange(100,255)) for i in range(30)]
arrX = [(x+1)*15 for x in range(30)]
Game = True

def draw(x, y, clr):
    comb = zip(y, clr, x)
    for y, c, x in comb:
        pygame.draw.line(display_surface, c, (x, height), (x, height - y), 3)

def check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

while Game:
    keys = pygame.key.get_pressed() 
    check()
    if keys[pygame.K_SPACE]:
        running = True

    if running == False:
        display_surface.fill((0,0,0))
        draw(arrX, arr, clr)
        pygame.display.update()

    else:

        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                check()
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1],arr[j]
                    clr[j], clr[j+1] = clr[j+1], clr[j]
                display_surface.fill((0,0,0))
                draw(arrX, arr, clr)
                pygame.draw.line(display_surface, WHITE, (arrX[j+1], height), (arrX[j+1], height - arr[j+1]), 3)
                pygame.time.delay(50)
                pygame.display.update()
        running = False

    clock.tick(20)

pygame.quit()


