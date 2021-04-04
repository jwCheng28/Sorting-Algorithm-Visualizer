import pygame
import random
from algorithms import Algorithms

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BAR_HEIGHT_RANGE = (10, 40)
BAR_COLOR_RANGE = (100, 255)
BAR_AMOUNT = 60

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")
pygame.display.update()
clock = pygame.time.Clock()

algo = Algorithms(
    WINDOW_WIDTH, WINDOW_HEIGHT,
    BAR_HEIGHT_RANGE, BAR_COLOR_RANGE, BAR_AMOUNT,
    display_surface)

running = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if not running:
        display_surface.fill((0,0,0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        running = True
        display_surface.fill((0,0,0))
        algo.createBars()
        algo.drawBars()
    elif keys[pygame.K_s]:
        algo.selectionSort()
    elif keys[pygame.K_b]:
        algo.bubbleSort()
    elif keys[pygame.K_m]:
        algo.mergeSort(algo.barH, 0, algo.barAmount-1)
    elif keys[pygame.K_q]:
        pygame.quit()
        quit()

    pygame.display.update()
    clock.tick(15)
