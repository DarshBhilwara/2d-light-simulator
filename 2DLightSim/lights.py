import pygame
import math
import numpy


pygame.init()


class Lights:
    def __init__(self, x, y, color, intensity):
        self.x = x
        self.y = y
        self.color = color
        self.intensity = intensity
        self.type = "Lights"

    def lighting(self, screen, brightness, objects, mirrors):
        for i in range(720):
            angle = 2 * math.pi * i / 360
            rayx = self.x
            rayy = self.y

            raydx = math.cos(angle)
            raydy = math.sin(angle)

            ray_length = 0

            while ray_length < 800:
                rayx += raydx
                rayy += raydy

                for obj in objects:
                    if math.sqrt((rayx - obj[0])**2 + (rayy - obj[1])**2) <= obj[2]:
                        ray_length = 1000
                        break

                for obj in mirrors:
                    if 0 <= abs(rayx - obj.x) <= 1 and obj.y - obj.length/2 <= int(rayy) <= obj.y + obj.length/2:
                        angle = obj.reflect(self, angle)
                        raydx = math.cos(angle)
                        raydy = math.sin(angle)

                if (int(rayx) >= 720 or int(rayx) < 0 or int(rayy) >= 720 or int(rayy) < 0):
                    break

                brightness[int(rayx)][int(
                    rayy)] += (self.intensity/(ray_length + 0.0001))
                intense = min(255, int(brightness[int(rayx)][int(rayy)])*10)
                screen.set_at((int(rayx), int(rayy)),
                              (intense, intense, intense))

                ray_length += 1
