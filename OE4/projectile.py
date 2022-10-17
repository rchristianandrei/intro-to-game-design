from object import Object
import pygame


class Projectile(Object):

    def __init__(self, x, y, w, h):
        Object.__init__(self, x, y, w, h)

        self.sprites = None
        self.active_sprite = None

        self.scale = None
        self.rotation = None

        self.flip = None
        self.available = None

        self.speed = 15

    def move(self):
        # Check if projectile is within the frame
        inside = self.x > Object.west_bound - self.w * 3 \
                 and Object.east_bound(self.x, self.w, Object.width + self.w * 3)

        if inside:
            if self.flip:
                self.x -= self.speed
                self.active_sprite = pygame.transform.rotate(self.sprites, 180)
            else:
                self.x += self.speed
                self.active_sprite = self.sprites
            self.available = False
        else:
            self.available = True

    def update(self, character):

        # Update coordinates
        y = character.y + character.h / 2

        if character.flip:
            x = character.x
        else:
            x = character.x

        self.x = x
        self.y = y
        self.flip = character.flip

    def resize_sprite(self):
        self.sprites = pygame.transform.scale(self.sprites, self.scale)
        self.sprites = pygame.transform.rotate(self.sprites, self.rotation)
        self.active_sprite = self.sprites
