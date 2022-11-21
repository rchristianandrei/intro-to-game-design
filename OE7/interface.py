from object import Object


class UI(Object):

    canvas = {}
    font = None

    def __init__(self, name, x, y):
        super().__init__()

        self.name = name
        self.surface = ''
        self.rect = None
        self.x = x
        self.y = y
        self.rect = None

        UI.canvas.update({self.name: self})

    def update(self):
        self.rect = UI.font.render(self.surface, True, (255, 255, 255))

        self.w = self.rect.get_width()
        self.h = self.rect.get_height()

    def change_surface(self, text: str):
        self.surface = text
