import math
import pygame


class Mirror:
    def __init__(self, x, y, length, surface):
        self.x = x
        self.y = y
        self.length = length
        self.type = "Mirror"
        pygame.draw.line(surface, (0, 0, 255),
                         (x, y + length/2), (x, y - length/2), 3)

    def reflect(self, light, ray_angle):

        if math.pi > ray_angle >= 0:
            return math.pi - ray_angle
        else:
            return 3*math.pi - ray_angle
