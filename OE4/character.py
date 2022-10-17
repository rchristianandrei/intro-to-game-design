from object import Object
import pygame
import copy


class Character(Object):

    def __init__(self, x, y, w, h):
        Object.__init__(self, x, y, w, h)

        # Hotkey
        self.move = None

        # Flags
        self.jumping = False
        self.walking = False
        self.down = False
        self.old_y = None
        self.jump_count = 0

        # Sprites
        self.IDLE = []
        self.idle_scale = None

        self.RUN = []
        self.run_scale = None

        self.JUMP = []
        self.jump_scale = None
        self.jump_counter = 0

        self.active_sprite = None
        self.counter = 0

    def update(self):
        # Counter
        self.count()

        # Movement
        self.movement()

        # Animation
        self.animation()

    def count(self):
        if Object.counter % 3 == 0:
            self.counter += 1

        if self.counter > 9:
            self.counter = 0

    def movement(self):
        if not self.jumping:
            if self.move[4]:
                self.jumping = True
                self.do_jump()
                return

            self.y += Object.move_shape(self.move[0], self.y > Object.north_bound, -Object.speed)
            self.y += Object.move_shape(self.move[1], Object.south_bound(self.y, self.h, Object.height), Object.speed)
        else:
            self.do_jump()

        if self.move[3]:
            self.flip = False
        elif self.move[2]:
            self.flip = True

        self.x += Object.move_shape(self.move[2], self.x > Object.west_bound, -Object.speed)
        self.x += Object.move_shape(self.move[3], Object.east_bound(self.x, self.w, Object.width), Object.speed)

        if self.move[0] or self.move[1] or self.move[2] or self.move[3]:
            self.walking = True
        else:
            self.walking = False

    def animation(self):
        if self.jumping:
            self.jump_animation()
        elif self.walking:
            self.walk_animation()
        else:
            self.idle_animation()

    def do_jump(self):
        # Check if empty
        if self.old_y is None:
            self.old_y = copy.deepcopy(self.y)

        # Check if character can jump normally
        if (self.old_y + Object.jump_force) < Object.north_bound:
            target = Object.north_bound
        else:
            target = self.old_y + Object.jump_force

        # Check if reached peak
        if (self.y >= target) and not self.down:
            self.y -= Object.speed
        else:
            self.down = True

            if self.y <= self.old_y:
                self.y += Object.speed
            else:
                # Check if returned to old y
                if self.y > self.old_y:
                    self.y = self.old_y

                # Check if passed south bound
                if not Object.south_bound(self.y, self.h, Object.height):
                    self.y = Object.height - (self.h + 10)

                self.jumping = self.down = False
                self.old_y = None
                self.jump_counter = 0

    def resize_sprites(self):
        for x in range(10):
            self.IDLE[x] = pygame.transform.scale(self.IDLE[x], self.idle_scale)
            self.RUN[x] = pygame.transform.scale(self.RUN[x], self.run_scale)
            self.JUMP[x] = pygame.transform.scale(self.JUMP[x], self.jump_scale)

    def idle_animation(self):
        if self.flip:
            temp = pygame.transform.flip(self.IDLE[self.counter], True, False)
        else:
            temp = self.IDLE[self.counter]

        self.w = self.idle_scale[0]
        self.h = self.idle_scale[1]
        self.active_sprite = temp

    def walk_animation(self):
        if self.flip:
            temp = pygame.transform.flip(self.RUN[self.counter], True, False)
        else:
            temp = self.RUN[self.counter]

        self.w = self.run_scale[0]
        self.h = self.run_scale[1]
        self.active_sprite = temp

    def jump_animation(self):
        if Object.counter % 6 == 0:
            self.jump_counter += 1

        if self.jump_counter > 9:
            self.jump_counter = 0

        if self.flip:
            temp = pygame.transform.flip(self.JUMP[self.jump_counter], True, False)
        else:
            temp = self.JUMP[self.jump_counter]

        self.w = self.jump_scale[0]
        self.h = self.idle_scale[1]
        self.active_sprite = temp
