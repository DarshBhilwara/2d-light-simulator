import pygame
import numpy as np
import math
from lights import Lights
from mirror import Mirror

pygame.init()
pygame.display.set_caption("Light")

width = 720
height = 720

screen = pygame.display.set_mode((width, height))

clock, fps = pygame.time.Clock(), 60

surface = pygame.Surface((720, 720), pygame.SRCALPHA)
surface.fill((0, 0, 0, 0))
# light = Lights(400, 300, 240, 500)
# light2 = Lights(500, 400, 240, 500)
brightness = np.zeros((width, height), dtype=np.float32)
# mirror1 = Mirror(200, 250, 75, surface)
# objects = [(300, 400, 20)]
objects = []
# mirrors = [mirror1]
mirrors = []
running = True


def button(x, y, txt, fn):
    white = (255, 255, 255)
    gray = (150, 150, 150)
    black = (0, 0, 0)
    font = pygame.font.Font(None, 36)
    button_rect = pygame.Rect(x, y, 100, 60)  # x, y, width, height
    button_color = white
    button_text = txt
    button_hover_color = gray
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()[0]
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, button_hover_color, button_rect)
        if mouse_clicked:
            pass  # call the funciton needed (fn)
    else:
        pygame.draw.rect(screen, button_color, button_rect)
    text_surface = font.render(button_text, True, black)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)


while running:

    brightness.fill(0)
    button(36, 620, 'Reset', 'resetfunction')
    button(210, 620, 'Light', 'lightfunction')
    button(384, 620, 'Object', 'objectfunction')
    button(558, 620, 'Mirror', 'mirrorfunction')
    for obj in objects:
        pygame.draw.circle(surface, (255, 0, 0), (obj[0], obj[1]), obj[2])

    # light.lighting(screen, brightness, objects, mirrors)
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
