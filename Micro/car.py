import pygame
import random
import math
class car:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width=10
        self.height=10

        self.speed_range = (1,4)
        self.vel=random.randint(*self.speed_range)



        self.circles = [
            {"x": self.x, "y": self.y, "radius": 10, "color": (255, 0, 0)},  # Main circle
            {"x": self.x, "y": self.y - 15, "radius": 5, "color": (0, 255, 0)},
            {"x": self.x, "y": self.y - 15, "radius": 5, "color": (0, 255, 0)}# Additional circle
        ]
    def collided(self,end_x,end_y):
        if end_x >= self.x and end_x <= self.x + self.width and end_y >= self.y and end_y <= self.y + self.height:
            return True

    def distance(self, x2, y2):
        return math.sqrt(((float(self.x) - float(y2)) ** 2) + ((float(self.y) - float(x2)) ** 2))

    #def draw_circels(self, screen):
        #for circle in self.circles:
            #pygame.draw.circle(screen, circle["color"], (int(circle["x"]), int(circle["y"])), circle["radius"])
            #circle["x"] = circle["x"]+self.vel









