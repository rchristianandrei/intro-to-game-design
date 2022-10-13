import copy


class Object:

    speed = 0.3
    jump_force = -150
    north_bound, west_bound = 10, 10
    width = None
    height = None

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

    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.jump = False
        self.moving = None
        self.down = False
        self.old_y = None
        self.jump_count = 0

    def move(self):
        if not self.jump:
            if self.moving[4]:
                self.jump = True
                self.do_jump()
                return

            self.y += Object.move_shape(self.moving[0], self.y > Object.north_bound, -Object.speed)
            self.y += Object.move_shape(self.moving[1], Object.south_bound(self.y, self.h, Object.height), Object.speed)
        else:
            self.do_jump()

        self.x += Object.move_shape(self.moving[2], self.x > Object.west_bound, -Object.speed)
        self.x += Object.move_shape(self.moving[3], Object.east_bound(self.x, self.w, Object.width), Object.speed)

    def do_jump(self):

        target = None

        if self.old_y is None:
            self.old_y = copy.deepcopy(self.y)

        if (self.old_y + Object.jump_force) < Object.north_bound:
            target = Object.north_bound
        else:
            target = self.old_y + Object.jump_force

        if (self.y >= target) and not self.down:
            if self.y > Object.north_bound:
                self.y -= Object.speed
        else:
            self.down = True

            if self.y <= self.old_y:
                self.y += Object.speed
            else:
                self.jump = self.down = False
                self.old_y = None
