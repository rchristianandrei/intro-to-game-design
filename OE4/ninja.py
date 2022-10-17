from character import Character
from object import Object
import pygame


class Ninja(Character):

    def __init__(self, x, y, w, h, kunai):
        Character.__init__(self, x, y, w, h)

        self.kunai = kunai

        self.THROW = []
        self.throw_scale = None
        self.throw_counter = 0
        self.throwing = False

    def update(self):
        if self.move[5] and not self.throwing:
            self.throw_kunai()

        super().update()

    def animation(self):
        if self.throwing:
            self.throw_animation()
        elif self.jumping:
            self.jump_animation()
        elif self.walking:
            self.walk_animation()
        else:
            self.idle_animation()

    def throw_kunai(self):

        if self.kunai.available:
            self.kunai.update(self)
            self.throwing = True
        else:
            self.throwing = False

    def throw_animation(self):
        if self.flip:
            temp = pygame.transform.flip(self.THROW[self.throw_counter], True, False)
        else:
            temp = self.THROW[self.throw_counter]

        self.w = self.throw_scale[0]
        self.h = self.throw_scale[1]
        self.active_sprite = temp

        if Object.counter % 3 == 0:
            self.throw_counter += 1

        if self.throw_counter > 9:
            self.throw_counter = 0
            self.throwing = False

    def resize_sprites(self):
        super().resize_sprites()

        for x in range(10):
            self.THROW[x] = pygame.transform.scale(self.THROW[x], self.throw_scale)
