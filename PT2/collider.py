import setuptools.msvc

from settings import Settings
from object import Object
import pygame


class Collider(Object):

    def __init__(self):
        super().__init__()
        # Check this later
        self.active_collision = True
        self.rect = pygame.Rect(self.actual_x(), self.actual_y(), self.w, self.h)
        self.hit = []
        self.enter = []

    def update(self):
        super().update()

        if not self.active_collision:
            return

        self.rect = pygame.Rect(self.actual_x(), self.actual_y(), self.w, self.h)

        # Get objects that collided
        for obj in Settings.GAMEOBJECTS.values():
            if not obj.name == self.name:
                if obj.active and obj.rect is not None:
                    if self.rect.colliderect(obj):
                        self.hit.append(obj)

        for obj in self.hit:
            if not any(x.name == obj.name for x in self.enter):
                self.on_collide(obj)
                self.enter.append(obj)

        new_list = list(set(self.enter) - set(self.hit))
        self.enter = list(set(self.enter) - set(new_list))
        self.hit.clear()

    def on_collide(self, obj: Object):
        pass
