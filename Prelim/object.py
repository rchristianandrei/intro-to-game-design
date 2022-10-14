import copy
import pygame


class Object:
    speed = 4
    jump_force = -100
    north_bound, west_bound = 10, 10
    width = None
    height = None
    scale = (77, 146)
    counter = 1

    @staticmethod
    def move_shape(key, cond, speed):
        if key and cond:
            return speed
        return 0

    @staticmethod
    def south_bound(y, h, height):
        return y < height - (h + 10)

    @staticmethod
    def east_bound(x, w, width):
        return x < width - (w + 10)

    def __init__(self, x, y):
        # Movement
        self.jump = False
        self.moving = None
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
        self.flip = None
        self.counter = 0

        # Primary Settings
        self.x = x
        self.y = y
        self.w = None
        self.h = None

    def move(self):
        self.update_counter()

        if not self.jump:
            if self.moving[4]:
                self.jump = True
                self.do_jump()
                return

            self.y += Object.move_shape(self.moving[0], self.y > Object.north_bound, -Object.speed)
            self.y += Object.move_shape(self.moving[1], Object.south_bound(self.y, self.h, Object.height), Object.speed)
        else:
            self.do_jump()

        if self.moving[3]:
            self.flip = False
        elif self.moving[2]:
            self.flip = True

        self.x += Object.move_shape(self.moving[2], self.x > Object.west_bound, -Object.speed)
        self.x += Object.move_shape(self.moving[3], Object.east_bound(self.x, self.w, Object.width), Object.speed)

        if not self.jump:
            if not (self.moving[0]) and not (self.moving[1]) and not (self.moving[2]) \
                    and not (self.moving[3]):
                self.idle_animation()
            else:
                self.walk_animation()
        else:
            self.jump_animation()

    def do_jump(self):
        target = None

        # Check if empty
        if self.old_y is None:
            self.old_y = copy.deepcopy(self.y)

        # Check if can jump normally
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

                self.jump = self.down = False
                self.old_y = None
                self.jump_counter = 0

    def resize_sprites(self):
        for x in range(10):
            self.IDLE[x] = pygame.transform.scale(self.IDLE[x], self.idle_scale)
            self.RUN[x] = pygame.transform.scale(self.RUN[x], self.run_scale)
            self.JUMP[x] = pygame.transform.scale(self.JUMP[x], self.jump_scale)

    def update_counter(self):
        if Object.counter % 3 == 0:
            self.counter += 1

        if self.counter > 9:
            self.counter = 0

    def idle_animation(self):
        temp = None

        if self.flip:
            temp = pygame.transform.flip(self.IDLE[self.counter], True, False)
        else:
            temp = self.IDLE[self.counter]

        self.w = self.idle_scale[0]
        self.h = self.idle_scale[1]
        self.active_sprite = temp

    def walk_animation(self):
        temp = None

        if self.moving[2]:
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

        temp = None

        if self.flip:
            temp = pygame.transform.flip(self.JUMP[self.jump_counter], True, False)
        else:
            temp = self.JUMP[self.jump_counter]

        self.w = self.jump_scale[0]
        self.h = self.idle_scale[1]
        self.active_sprite = temp
