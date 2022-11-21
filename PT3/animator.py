from object import Object
import pygame


class Animation:

    def __init__(self, scale: tuple):
        self.sprites = []
        self.counter = 0
        self.modulus = 5
        self.scale = scale
        self.loop = True

    def resize(self):

        for i in range(len(self.sprites)):
            self.sprites[i] = pygame.transform.scale(self.sprites[i], self.scale)

    def rotate(self, angle: float):
        for i in range(len(self.sprites)):
            self.sprites[i] = pygame.transform.rotate(self.sprites[i], angle)


class Animator:
    counter = 0
    limit = 9999

    def __init__(self):
        self.animations: {str, Animation} = {}
        self.active_animation = ''
        self.active_sprite = None

    def add_animation(self, key: str, value: Animation):
        self.animations.update({key: value})

        if self.active_animation is None:
            self.active_animation = self.animations.get(key)

    def get_current_counter(self, key: str):

        return self.animations.get(key).counter

    def get_last_counter(self, key: str):

        return len(self.animations.get(key).sprites) - 1

    # Should be called every frame
    def animate(self, key: str, game_object: Object):
        if not key == self.active_animation:
            if not self.active_animation == '':
                self.animations.get(self.active_animation).counter = 0
            self.active_animation = key

        active: Animation = self.animations.get(key)

        self.active_sprite = pygame.transform.flip(
            active.sprites[active.counter], game_object.flip, False
        )
        game_object.w = active.scale[0]
        game_object.h = active.scale[1]

        if Animator.counter % active.modulus == 0:
            if active.counter < len(active.sprites) - 1:
                active.counter += 1
            else:
                if active.loop:
                    active.counter = 0
                else:
                    active.counter -= 1
