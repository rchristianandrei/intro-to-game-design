from animator import Animator, Animation
from collider import Collider
from settings import Settings
from object import Object
import pygame


class Bird(Collider):

    def __init__(self):
        super().__init__()

        player = Settings.GAMEOBJECTS.get(Settings.player_name)

        self.y = Object.ground + player.jump_force
        self.speed = 5
        self.animator = Animator()

        # Animation
        self.RUN = 'Run'
        self.animator.animations.update({self.RUN: Animation((78, 57))})

        for x in range(6):
            self.animator.animations.get(self.RUN).sprites.append(
                pygame.image.load(f'../images/bird/Walk_{x}.png')
            )

        for animation in self.animator.animations.values():
            animation.resize()

    def update(self):
        super().update()

        if self.flip:
            can_move = self.x > -self.w
        else:
            can_move = self.x < Settings.WIDTH

        if can_move:
            if self.flip:
                self.x -= self.speed
            else:
                self.x += self.speed
        else:
            self.flip = not self.flip

        self.animator.animate(self.RUN, self)

    def on_collide(self, obj):
        if not obj.tag == 'Player' or not Settings.RUNNING:
            return

        if (self.flip and self.x < obj.x) or (not self.flip and self.x > obj.x):
            return

        Settings.BIRD_SOUND.play()
        obj.dead(0.5)
