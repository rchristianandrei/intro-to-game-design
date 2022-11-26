
from animator import Animator, Animation
from collider import Collider
from settings import Settings
import pygame
import random


class Buff(Collider):

    def __init__(self):
        super().__init__()
        self.y = 0

        self.added_hp = 2
        self.speed = 1
        self.animator = Animator()

        self.IDLE = 'Idle'
        self.animator.animations.update({self.IDLE: Animation((32, 32))})
        anim = self.animator.animations.get(self.IDLE)
        anim.sprites.append(pygame.image.load('../images/food/sashimi.png'))
        anim.resize()

    def update(self):
        super().update()

        if self.y < Settings.HEIGHT:
            self.y += self.speed
        else:
            self.active = False

        self.animator.animate(self.IDLE, self)

    def reuse(self):
        self.active = True
        self.y = 0

    def on_collide(self, obj):
        if not Settings.RUNNING:
            return

        if obj.tag == 'Player':
            hp = obj.health
            if hp.get_hp() < hp.MAX_HP:
                hp.decrease_hp(-self.added_hp)

            if hp.get_hp() > hp.MAX_HP:
                hp.health = hp.MAX_HP

        self.active = False


class BuffManager:

    def __init__(self):
        self.duration = None
        self.last_check = None
        self.min = 8
        self.max = 15
        self.name = 'Buff_'
        self.index = 0

    def update(self):
        if not Settings.RUNNING:
            return

        if self.duration is None:
            self.duration = random.randrange(self.min, self.max)
            self.last_check = pygame.time.get_ticks() / 1000

        if pygame.time.get_ticks() / 1000 - self.last_check > self.duration:
            buff = self.get_buff()
            buff.reuse()
            buff.x = random.randrange(0, Settings.WIDTH)
            self.index += 1
            self.duration = None

    def get_buff(self):
        target = None

        for buff in Settings.GAMEOBJECTS.values():
            if isinstance(buff, Buff) and not buff.active:
                target = buff

        if target is None:
            target = Buff()
            Settings.GAMEOBJECTS.update({self.name + str(self.index): target})

        return target
