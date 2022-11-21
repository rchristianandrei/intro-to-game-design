from animator import Animator, Animation
from settings import Settings
from enemy import Enemy
import pygame


class GameManager:

    def __init__(self):
        self.RUN = 'Run'
        self.ATTACK = 'Attack'
        self.DEAD = 'Dead'

        # Animators
        self.animators = [
            Animator(), Animator()
        ]

        # Animations
        self.animators[0].animations.update({self.RUN: Animation((110, 146))})
        self.animators[0].animations.update({self.ATTACK: Animation((150, 161))})
        self.animators[0].animations.update({self.DEAD: Animation((165, 171))})
        self.animators[0].animations.get(self.DEAD).loop = False

        self.animators[1].animations.update({self.RUN: Animation((110, 146))})
        self.animators[1].animations.update({self.ATTACK: Animation((150, 161))})
        self.animators[1].animations.update({self.DEAD: Animation((165, 171))})
        self.animators[1].animations.get(self.DEAD).loop = False

        # Populate the animations
        load = pygame.image.load
        anim1 = self.animators[0].animations
        anim2 = self.animators[1].animations
        for x in range(10):
            anim1.get(self.RUN).sprites.append(load(f'../images/object3/Run/Run__00{x}.png'))
            anim1.get(self.ATTACK).sprites.append(load(f'../images/object3/Attack/Attack__00{x}.png'))
            anim1.get(self.DEAD).sprites.append(load(f'../images/object3/Dead/Dead__00{x}.png'))

            anim2.get(self.RUN).sprites.append(load(f'../images/object1/Run/Run__00{x}.png'))
            anim2.get(self.ATTACK).sprites.append(load(f'../images/object1/Attack/Attack__00{x}.png'))
            anim2.get(self.DEAD).sprites.append(load(f'../images/object1/Dead/Dead__00{x}.png'))

        # Resize Animations
        for i in self.animators:
            for j in i.animations.values():
                j.resize()

    def spawn_enemies(self):

        Settings.GAMEOBJECTS.update({'Enemy_0': Enemy('Enemy_0', True, self.animators[0])})
        Settings.GAMEOBJECTS.update({'Enemy_1': Enemy('Enemy_1', False, self.animators[1])})

    @staticmethod
    def check_if_win():
        if not Settings.RUNNING:
            return

        enemies = 0

        for enemy in Settings.GAMEOBJECTS.values():
            if not isinstance(enemy, Enemy):
                continue

            if enemy.active:
                enemies += 1

        if enemies == 0:
            # You won
            Settings.MESSAGE = Settings.WIN
            Settings.RUNNING = False
