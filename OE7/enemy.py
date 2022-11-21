import pygame.image

from animator import Animation, Animator
from collider import Collider
from settings import Settings
from health import Health
from ninja import Ninja


class Enemy(Collider):

    def __init__(self, name: str, flip: bool):
        super().__init__()

        self.speed = 2
        hp = 2
        self.duration = 2
        self.tag = 'Enemy'
        self.last_shown = None
        self.name = name
        self.flip = flip

        # Health Component
        self.health = Health(self, hp)

        # Animator Component
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

        # Update Animation
        self.animator.animate(self.state)

        # Stop the loop of attack animation if game is not over
        if self.state == self.ATTACK and Settings.RUNNING:
            if self.animator.get_current_counter(self.ATTACK) >= self.animator.get_last_counter(self.ATTACK):
                self.state = self.RUN

        # Countdown before disappearing on screen
        if self.state == self.DEAD:
            if self.last_shown is None:
                self.last_shown = pygame.time.get_ticks() / 1000
            elif (pygame.time.get_ticks() / 1000) - self.last_shown > self.duration:
                self.last_shown = None
                self.active = False

        # Keep the Health Bar updated
        self.health.update()

    def dead(self) -> bool:
        if not self.state == self.DEAD:
            self.health.decrease_hp(1)

        if self.health.get_hp() <= 0:
            self.active_collision = False
            self.state = self.DEAD

            Settings.DEATH_SOUND.play()
            return True
        return False

    def on_collide(self, obj: Ninja):
        if self.state == self.DEAD or not obj.tag == 'Player':
            return

        if (self.flip and self.x < obj.x) or (not self.flip and self.x > obj.x):
            return

        self.state = self.ATTACK
        obj.dead()

    def reset(self, flip, x):
        self.state = self.RUN
        self.flip = flip
        self.x = x
        self.health.reset()
        self.active = True
        self.active_collision = True
