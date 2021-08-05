import pygame
import random

class Snake:
    headColor = (50, 255, 0)
    bodyColor = (0, 200, 0)
    damageColor = (255, 0, 0)

    def __init__(self, field, color, length=5, x=10, y=10):
        self.field = field
        self.body = []
        self.growLength = 0
        for i in range(0, length):
            self.body.append((x - i, y))
        self.bodyColor = ((color & 0xFF0000) / 256 ** 2, ((color & 0x00FF00) / 256) % 256, color & 0x0000FF)
        self.headColor = ((color & 0xFF0000) / 256 ** 2, ((color & 0x00FF00) / 256) % 256, color & 0x0000FF)

    def move(self, dx, dy):
        (x, y) = self.body[0]
        x += dx
        y += dy
        if self.growLength > 0:
            self.growLength -= 1
        else:
            self.body.pop()
        self.body.insert(0, (x, y))
        if self.body[0] in self.body[1:]:
            return False
        elif x < 0 or x >= self.field.width or y < 0 or y >= self.field.height:
            return False
        else:
            return True

    def grow(self, length=1):
        self.growLength = length

    def draw(self, damage = False):
        for i in range(0, len(self.body)):
            if damage:
                color = self.damageColor
            elif i == 0:
                color = self.headColor
            else:
                color = self.bodyColor

            (x, y) = self.body[i]
            size = self.field.blockSize
            rect = (x * size, y * size, size, size)
            pygame.draw.rect(self.field.screen, color, rect, 0)


class Field():
    fieldColor = (0, 50, 0)

    def __init__(self, screen, width, height, blockSize,color = 12800):
        self.screen = screen
        self.width = width
        self.height = height
        self.blockSize = blockSize
        self.fieldColor = ((color & 0xFF0000) / 256 **2, ((color & 0x00FF00) / 256) % 256, color & 0x0000FF)

    def draw(self):
        self.screen.fill(self.fieldColor)


class Food():
    foodColor = (0, 255, 255)

    def __init__(self, field):
        self.field = field
        self.x = random.randint(0, field.width - 1)
        self.y = random.randint(0, field.height - 1)
        self.color = self.foodColor

    def draw(self):
        size = self.field.blockSize
        rect = (self.x * size, self.y * size, size, size)
        pygame.draw.rect(self.field.screen, self.color, rect, 0)


