from animation import Animation
from object import Object
import pygame


class Enemy(Object):

    jump_height = -100

    def __init__(self, x, y, w, h, speed):

        # Animations
        self.IDLE = Animation()
        self.RUN = Animation()
        self.JUMP = Animation()
        self.THROW = Animation()

        # Jump
        self.old_y = None
        self.going_down = False

        # Flags
        self.running = False
        self.jumping = False
        self.go_right = True

        Object.__init__(self, x, y, w, h, speed)

    def update(self):

        # Movement
        self.movement()

        # Animation
        self.animation()

        # Check Settings

    def movement(self):

        if self.go_right:
            if self.east_boundary():
                self.x += self.speed
            else:
                self.go_right = False
        else:
            if self.west_boundary():
                self.x -= self.speed
            else:
                self.go_right = True

    def animation(self):

        if self.jumping:

            # Jump Animation
            self.JUMP.update()

            if self.flip:
                self.active_sprite = pygame.transform.flip(self.JUMP.sprites[self.JUMP.counter], True, False)
            else:
                self.active_sprite = self.JUMP.sprites[self.JUMP.counter]

            self.w = self.JUMP.scale[0]
            self.h = self.JUMP.scale[1]

        elif self.running:

            # Run Animation
            self.RUN.update()

            if self.flip:
                self.active_sprite = pygame.transform.flip(self.RUN.sprites[self.RUN.counter], True, False)
            else:
                self.active_sprite = self.RUN.sprites[self.RUN.counter]

            self.w = self.RUN.scale[0]
            self.h = self.RUN.scale[1]
            self.IDLE.counter = 0

        else:

            # Idle Animation
            self.IDLE.update()

            if self.flip:
                self.active_sprite = pygame.transform.flip(self.IDLE.sprites[self.IDLE.counter], True, False)
            else:
                self.active_sprite = self.IDLE.sprites[self.IDLE.counter]

            self.w = self.IDLE.scale[0]
            self.h = self.IDLE.scale[1]
            self.RUN.counter = 0
