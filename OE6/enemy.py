from animation import Animation
from object import Object
from ninja import Ninja
import pygame


class Enemy(Object):

    jump_height = -100

    def __init__(self, x, y, w, h, speed):

        # Animations
        self.RUN = Animation()
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
                self.flip = True
        else:
            if self.west_boundary():
                self.x -= self.speed
            else:
                self.go_right = True
                self.flip = False

    def animation(self):

        # Run Animation
        self.RUN.update()

        if self.flip:
            self.active_sprite = pygame.transform.flip(self.RUN.sprites[self.RUN.counter], True, False)
        else:
            self.active_sprite = self.RUN.sprites[self.RUN.counter]

        self.w = self.RUN.scale[0]
        self.h = self.RUN.scale[1]

    def detect_collision(self, game_objects):

        for x in game_objects:
            if self.rect.colliderect(x) and isinstance(x, Ninja):
                print(f"This Enemy collided with {x}")
