from object import Object
from animation import Animation
import pygame
import copy


class Character(Object):

    jump_height = -100

    def __init__(self, x, y, w, h, speed):

        # Hotkey
        self.hotkey = None

        # Animations
        self.active_sprite = None

        self.IDLE = Animation()
        self.RUN = Animation()
        self.JUMP = Animation()

        # Jump
        self.old_y = None
        self.going_down = False

        # Flags
        self.running = False
        self.jumping = False

        Object.__init__(self, x, y, w, h, speed)

    def update(self):

        # Movement
        self.movement()

        # Animation
        self.animation()

        # Check Settings

    def movement(self):

        if self.hotkey[4] and not self.jumping:
            self.jumping = True

        if self.jumping:
            self.do_jump()

        if self.hotkey[0] or self.hotkey[1] or self.hotkey[2] or self.hotkey[3]:

            # Vertical Movement
            if self.hotkey[0] and self.north_boundary() and not self.jumping:
                self.y -= self.speed
            elif self.hotkey[1] and self.south_boundary() and not self.jumping:
                self.y += self.speed

            # Horizontal Movement
            if self.hotkey[2] and self.west_boundary():
                self.x -= self.speed
            elif self.hotkey[3] and self.east_boundary():
                self.x += self.speed

            # Update Parameters
            if self.hotkey[2]:
                self.flip = True
            elif self.hotkey[3]:
                self.flip = False

            self.running = True

        else:
            self.running = False

    def do_jump(self):

        if self.old_y is None:
            self.old_y = copy.deepcopy(self.y)

        target = self.old_y + Character.jump_height

        if self.old_y + Character.jump_height < Object.offset:
            target = Object.offset

        if self.y > target and not self.going_down:
            self.y -= self.speed
            return

        self.going_down = True

        if self.y < self.old_y:
            self.y += self.speed
        else:
            if not self.y == self.old_y:
                self.y = self.old_y

            self.old_y = None
            self.going_down = False
            self.jumping = False
            self.JUMP.counter = 0

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
