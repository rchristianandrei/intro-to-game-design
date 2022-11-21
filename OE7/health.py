from settings import Settings
from object import Object
import pygame


class Health:

    def __init__(self, obj: Object, health: float):
        self.MAX_HP = self.health = health
        self.offset = 0
        self.width = 50
        self.height = 10
        self.health_percent = self.width / self.health
        self.GREEN = self.color = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.ORANGE = (255, 255, 0)
        self.object = obj
        self.rect = None

    def get_hp(self):

        return self.health

    def decrease_hp(self, amount: float):
        self.health -= amount
        self.width -= self.health_percent * amount

        if self.health <= self.MAX_HP * (1/3):
            self.color = self.RED
        elif self.health <= self.MAX_HP * (2/3):
            self.color = self.ORANGE

    def reset(self):
        self.health = self.MAX_HP
        self.width = self.health_percent * self.health
        self.color = self.GREEN

    def update(self):
        self.rect = pygame.Rect(
            self.object.x - self.width/2,
            self.object.y - self.object.h / 2 - self.offset,
            self.width,
            self.height
        )
