from animator import Animator, Animation
from settings import Settings
from enemy import Enemy
import pygame
import random


class GameManager:

    def __init__(self):
        self.level = 0
        self.enemies = [2, 3, 5]

    def spawn_enemies(self):
        name = 'Enemy_'
        for i in range(self.enemies[self.level]):
            speed = random.randrange(1, 5)
            rand = random.randint(0, 1)
            pos = random.choice([True, False])
            new = name + str(i)
            anim: Animator = GameManager.get_anim(rand)
            Settings.GAMEOBJECTS.update({new: Enemy(new, pos, anim)})

            if pos:
                Settings.GAMEOBJECTS.get(new).x = Settings.WIDTH
            else:
                Settings.GAMEOBJECTS.get(new).x = 0

            Settings.GAMEOBJECTS.get(new).speed = speed

    def check_if_win(self):
        if not Settings.RUNNING:
            return

        enemies = 0

        for enemy in Settings.GAMEOBJECTS.values():
            if not isinstance(enemy, Enemy):
                continue

            if enemy.active:
                enemies += 1

        if enemies == 0:
            if self.level == len(self.enemies)-1:
                # You won
                Settings.MESSAGE = Settings.WIN
                Settings.RUNNING = False
            else:
                self.level += 1
                Settings.RUNNING = True
                self.spawn_enemies()

    @staticmethod
    def get_anim(index: int) -> Animator:
        anim = Animator()

        run = 'Run'
        attack = 'Attack'
        dead = 'Dead'

        anim.animations.update({run: Animation((110, 146))})
        anim.animations.update({attack: Animation((150, 161))})
        anim.animations.update({dead: Animation((165, 171))})
        anim.animations.get(dead).loop = False

        load = pygame.image.load
        for x in range(10):
            if index == 0:
                anim.animations.get(run).sprites.append(load(f'../images/object3/Run/Run__00{x}.png'))
                anim.animations.get(attack).sprites.append(load(f'../images/object3/Attack/Attack__00{x}.png'))
                anim.animations.get(dead).sprites.append(load(f'../images/object3/Dead/Dead__00{x}.png'))
            else:
                anim.animations.get(run).sprites.append(load(f'../images/object1/Run/Run__00{x}.png'))
                anim.animations.get(attack).sprites.append(load(f'../images/object1/Attack/Attack__00{x}.png'))
                anim.animations.get(dead).sprites.append(load(f'../images/object1/Dead/Dead__00{x}.png'))

        for animation in anim.animations.values():
            animation.resize()

        return anim
