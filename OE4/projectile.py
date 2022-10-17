from object import Object


class Projectile(Object):

    def __int__(self, character, w, h):

        self.update()

        super().__init__(self, self.x, self.y, w, h)

        self.reference = character
        self.flip = character.flip
        self.available = True
        self.sprites = None

    def move(self):
        # Check if projectile is within the frame
        inside = self.x > Object.west_bound - 10 and Object.east_bound(self.x, self.w, Object.width) + 10

        if inside:
            if self.flip:
                self.x -= Object.speed
            else:
                self.x += Object.speed
            self.available = False
        else:
            self.available = True

    def update(self):

        # Update coordinates
        y = self.reference.y + self.reference.h / 2

        if self.reference.flip:
            x = self.reference.x
        else:
            x = self.reference.x + self.reference.w

        self.x = x
        self.y = y
