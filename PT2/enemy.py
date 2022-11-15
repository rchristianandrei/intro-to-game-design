import pygame.image

from animator import Animation, Animator
from collider import Collider
from settings import Settings
from ninja import Ninja


class Enemy(Collider):

    def __init__(self, name: str, flip: bool):
        super().__init__()

        self.speed = 2
        self.health = 2
        self.duration = 2
        self.tag = 'Enemy'
        self.last_shown = None
        self.name = name
        self.flip = flip

        self.health_rect = None
        self.health_bar_w = 50
        self.health_percentage = self.health_bar_w / self.health

        self.animator = Animator(self)
        self.RUN = 'Run'
        self.ATTACK = 'Attack'
        self.DEAD = 'Dead'
        self.state = self.RUN

        self.animator.animations.update({self.RUN: Animation((110, 146))})
        self.animator.animations.update({self.ATTACK: Animation((150, 161))})
        self.animator.animations.update({self.DEAD: Animation((165, 171))})

        anim = self.animator.animations
        anim.get(self.DEAD).loop = False

        load = pygame.image.load
        for x in range(10):
            anim.get(self.RUN).sprites.append(load(f'../images/object3/Run/Run__00{x}.png'))
            anim.get(self.ATTACK).sprites.append(load(f'../images/object3/Attack/Attack__00{x}.png'))
            anim.get(self.DEAD).sprites.append(load(f'../images/object3/Dead/Dead__00{x}.png'))

        for x in self.animator.animations.values():
            x.resize()

    def update(self):
        super().update()

        if self.flip:
            can_move = self.x > -self.w
        else:
            can_move = self.x < Settings.WIDTH

        if can_move:
            if self.state == self.RUN:
                if self.flip:
                    self.x -= self.speed
                else:
                    self.x += self.speed
        else:
            self.active = False

        self.animator.animate(self.state)

        if self.state == self.DEAD:
            if self.last_shown is None:
                self.last_shown = pygame.time.get_ticks() / 1000
            elif (pygame.time.get_ticks() / 1000) - self.last_shown > self.duration:
                self.last_shown = None
                self.active = False

        self.health_rect = pygame.Rect(self.x-self.health_bar_w/2, self.y-self.h/2, self.health_bar_w, 10)

    def dead(self) -> bool:
        if not self.state == self.DEAD:
            self.health -= 1
            self.health_bar_w -= self.health_percentage

        print(self.health)

        if self.health <= 0:
            self.active_collision = False
            self.state = self.DEAD
            return True
        return False

    def on_collide(self, obj: Ninja):
        if self.state == self.DEAD:
            return

        if obj.tag == 'Player':
            if (self.flip and self.x < obj.x) or (not self.flip and self.x > obj.x):
                return

            self.state = self.ATTACK
            obj.dead()

    def reset(self, flip, x):
        self.state = self.RUN
        self.flip = flip
        self.x = x
        self.health = 2
        self.health_bar_w = self.health * self.health_percentage

        self.active = True
        self.active_collision = True
