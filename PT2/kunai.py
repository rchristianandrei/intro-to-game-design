import pygame.image

from animator import Animation, Animator
from settings import Settings
from collider import Collider
from interface import UI


class Kunai(Collider):

    def __init__(self, name, owner):
        super().__init__()
        self.name = name
        self.owner = owner
        self.active = False

        self.speed = 10
        self.duration = 8
        self.last_shown = None

        self.score = 'Kills'
        UI.canvas.update({self.score: UI(self.score, Settings.WIDTH - 200, 100)})
        UI.canvas.get(self.score).change_surface(f'Score {Settings.SCORE}')

        # Animation
        self.animator = Animator(self)
        self.Ammo = 'Kunai'
        self.animator.animations.update({self.Ammo: Animation((80, 16))})

        anim = self.animator.animations.get(self.Ammo)
        anim.sprites.append(pygame.image.load('../images/object1/Kunai/Kunai.png'))
        anim.rotate(-90)
        anim.resize()

    def update(self):
        super().update()

        west = self.actual_x() > -self.w * 2
        east = self.actual_x() < Settings.WIDTH + self.w * 2

        # Movement
        if west and east:
            if self.flip:
                self.x -= self.speed
            else:
                self.x += self.speed
        elif self.last_shown is None:
            self.last_shown = pygame.time.get_ticks() / 1000

        if self.last_shown is not None:
            if (pygame.time.get_ticks() / 1000) - self.last_shown >= self.duration:
                self.owner.ammo += 1
                self.last_shown = None
                self.active = False

        # Animation
        self.animator.animate(self.Ammo)

    def throw(self):
        self.y = self.owner.y
        self.x = self.owner.x
        self.flip = self.owner.flip
        self.active = True

    def on_collide(self, obj):

        if obj.tag == 'Enemy' and obj.active_collision:
            # Kill the enemy
            self.y = -self.h

            if obj.dead():
                Settings.SCORE += 1
                UI.canvas.get(self.score).change_surface(f'Score {Settings.SCORE}')
