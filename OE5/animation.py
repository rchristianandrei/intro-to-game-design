import pygame


class Animation:

    global_counter = 0
    counter_limit = 1000
    reset_counter = 0

    def __init__(self):

        self.sprites = []
        self.scale = self.modulus = None
        self.counter = -1

    def update(self):

        if Animation.global_counter % self.modulus == 0:
            if self.counter > len(self.sprites) - 2:
                self.counter = Animation.reset_counter
            else:
                self.counter += 1

    def resize(self):

        for x in range(len(self.sprites)):
            self.sprites[x] = pygame.transform.scale(self.sprites[x], self.scale)
