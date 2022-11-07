class Object:

    # Limits
    offset = 10
    width = height = None

    def __init__(self, x, y, w, h, speed):

        # Settings
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.flip = False
        self.speed = speed
        self.active_sprite = None

        # Collision
        self.rect = None

    def north_boundary(self):
        return self.actual_y() > Object.offset

    def south_boundary(self):
        return self.actual_y() + self.h < Object.height - Object.offset

    def west_boundary(self):
        return self.actual_x() > Object.offset

    def east_boundary(self):
        return self.actual_x() + self.w < Object.width - Object.offset

    def actual_x(self):

        return self.x - self.w / 2

    def actual_y(self):

        return self.y - self.h / 2
