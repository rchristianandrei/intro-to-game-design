from settings import Settings
from object import Object
from enemy import Enemy
import pygame
import random


class EnemySpawnManager(Object):

    def __init__(self):
        super().__init__()

        self.index = 0
        self.min = 1
        self.max = 5
        self.duration = 0
        self.last_shown = None

    def update(self):
        if not Settings.RUNNING:
            return

        if self.last_shown is None:
            self.last_shown = pygame.time.get_ticks() / 1000
            self.duration = random.randrange(self.min, self.max)

        if (pygame.time.get_ticks() / 1000) - self.last_shown > self.duration:
            enemy = self.get_enemy()

            flip = random.choice([True, False])

            if flip:
                x = Settings.WIDTH
            else:
                x = 0

            enemy.reset(flip, x)

            self.last_shown = None

    def get_enemy(self) -> Enemy:
        enemy = None

        for e in Settings.GAMEOBJECTS.values():
            if not e.active and e.tag == 'Enemy':
                return e
            continue

        if enemy is None:
            num = self.index
            name = f'Enemy_{num}'
            enemy = Enemy(name, False)
            Settings.GAMEOBJECTS.update({name: enemy})
            self.index += 1

        return enemy
