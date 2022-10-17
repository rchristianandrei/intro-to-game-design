from character import Character
from projectile import Projectile
import pygame


class Ninja(Character):

    def __init__(self, x, y, w, h):
        super().__init__(self, x, y, w, h)

        load = pygame.image.load

        self.kunai = Projectile(self, 10, 10)
        self.kunai.sprites = load("../images/object1/Kunai/Kunai.png")

        self.sprites = []

        for x in range(x):
            self.sprites.append(load(f"../images/object1/Throw/Throw__00{x}.png"))

    def throw_kunai(self):

        if not self.jump and self.moving[5] and self.kunai.available:
            self.kunai.update()

