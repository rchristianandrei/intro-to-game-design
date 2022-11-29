from settings import Settings


class Object:

    ground = Settings.HEIGHT - 100

    def __init__(self):
        self.x: float = Settings.WIDTH / 2
        self.y: float = Object.ground
        self.w: float = 0
        self.h: float = 0
        self.flip: bool = False
        self.active: bool = True
        self.name = ''
        self.tag = ''

    def update(self):
        pass

    def north_boundary(self):
        return self.actual_y() > Settings.OFFSET

    def south_boundary(self):
        return self.actual_y() + self.h < Settings.HEIGHT - Settings.OFFSET

    def west_boundary(self):
        return self.actual_x() > Settings.OFFSET

    def east_boundary(self):
        return self.actual_x() + self.w < Settings.WIDTH - Settings.OFFSET

    def actual_x(self):
        return self.x - self.w / 2

    def actual_y(self):
        return self.y - self.h / 2
