import pygame
import numpy as np
import math
from objects import obj 
from lights import Lights
from mirror import Mirror

pygame.init()
pygame.display.set_caption("Light")

width = 720
height = 720

screen = pygame.display.set_mode((width, height))

clock, fps = pygame.time.Clock(), 1000

surface = pygame.Surface((720, 720), pygame.SRCALPHA)
surface.fill((0, 0, 0, 0))
light = Lights(400, 300, 240, 500)
light2 = Lights(500, 400, 240, 500)
brightness = np.zeros((width, height), dtype=np.float32)
mirror1 = Mirror(200, 250, 75, surface)
objects = [(300, 400, 20)]
mirrors = [mirror1]
running = True


while running:

    brightness.fill(0)

    for obj in objects:
        pygame.draw.circle(surface, (255, 0, 0), (obj[0], obj[1]), obj[2])

    light.lighting(screen, brightness, objects, mirrors)
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
