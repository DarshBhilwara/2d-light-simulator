import math


class Object:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def block(self, screen, brightness, light):
        for i in range(720):
            for j in range(720):
                if math.sqrt((i - self.x)**2 + (j - self.y)**2) <= self.radius:
                    brightness[i][j] == 0
                    screen.set_at((i, j), self.color)

        for i in range(720):
            for j in range(720):
                e = 0.0001
                dx = i - light.x
                dy = j - light.y
                dx1 = i - self.x
                dy1 = j - self.y

                distance = math.sqrt(dx**2 + dy**2)
                distance1 = math.sqrt(dx1**2 + dy1**2)
