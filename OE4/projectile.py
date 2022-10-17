from object import Object


class Projectile(Object):

    def __int__(self, character, w, h):

        # Spawn projectile
        y = character.y + character.h / 2

        if character.flip:
            x = character.x
        else:
            x = character.x + character.w

        Object.__init__(self, x, y, w, h)

        self.flip = character.flip

        sprites = []

    def move(self):
        # Check if projectile is within the frame
        inside = self.x > Object.west_bound and Object.east_bound(self.x, self.w, Object.width)

        if inside:
            if self.flip:
                self.x -= Object.speed
            else:
                self.x += Object.speed
        else:
            del self

