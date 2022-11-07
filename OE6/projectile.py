from animation import Animation
from object import Object
import pygame


class Projectile(Object):

    def __init__(self, x, y, w, h, speed):

        self.ready = True
        self.sprite = Animation()
        self.sprite.scale = (w, h)
        self.owner = None
        Object.__init__(self, x, y, w, h, speed)

    def update(self):

        west = self.actual_x() > Object.offset - self.h * 2
        east = self.actual_x() + self.w < Object.width - Object.offset + self.h * 2

        # Movement
        if west and east:

            self.ready = False

            if west and self.flip:
                self.x -= self.speed
            if east and not self.flip:
                self.x += self.speed
        else:
            self.ready = True
            self.owner.throwing = False

        # Animation
        if self.flip:
            self.active_sprite = pygame.transform.flip(self.sprite.sprites[self.sprite.counter], True, False)
        else:
            self.active_sprite = self.sprite.sprites[self.sprite.counter]

    def reset_position(self):
        self.y = self.owner.y
        self.x = self.owner.x
        self.flip = self.owner.flip

    def set_owner(self, owner):
        self.owner = owner

    def detect_collision(self, game_objects):
        for x in game_objects:
            if self.rect.colliderect(x) and (not self == x and not self.owner == x):
                print(f"This projectile collided with {x}")
