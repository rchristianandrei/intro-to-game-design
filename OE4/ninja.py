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

    def move(self):
        self.update_counter()

        # Moves
        if self.moving[5] and not self.jump:
            self.throw_kunai()
            self.throwing = True

        if not self.throwing:
            if not self.jump:
                # Jump
                if self.moving[4]:
                    self.jump = True
                    self.do_jump()
                    return

                # Move on Y
                self.y += Object.move_shape(self.moving[0], self.y > Object.north_bound, -Object.speed)
                self.y += Object.move_shape(self.moving[1], Object.south_bound(self.y, self.h, Object.height), Object.speed)
            else:
                self.do_jump()

            # Move on X
            if self.moving[3]:
                self.flip = False
            elif self.moving[2]:
                self.flip = True

            self.x += Object.move_shape(self.moving[2], self.x > Object.west_bound, -Object.speed)
            self.x += Object.move_shape(self.moving[3], Object.east_bound(self.x, self.w, Object.width), Object.speed)

        # Animation
        if not self.throwing:
            if not self.jump:
                if not (self.moving[0]) and not (self.moving[1]) and not (self.moving[2]) \
                        and not (self.moving[3]):
                    self.idle_animation()
                else:
                    self.walk_animation()
            else:
                self.jump_animation()
        else:
            self.throw_animation()

    def throw_kunai(self):

        if not self.jump and self.moving[5] and self.kunai.available:
            self.kunai.update(self)

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
