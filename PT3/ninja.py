from animator import Animation, Animator
from settings import Settings
from collider import Collider
from health import Health
from interface import UI
from kunai import Kunai
import pygame.key
import copy


class Ninja(Collider):

    def __init__(self, name):
        super().__init__()
        # Settings
        self.LEFT_KEY = pygame.K_a
        self.RIGHT_KEY = pygame.K_d
        self.JUMP_KEY = pygame.K_SPACE
        self.THROW_KEY = pygame.K_e
        self.name = name

        self.tag = 'Player'
        self.speed = 8
        self.jump_speed_up = 10
        self.jump_speed_down = self.jump_speed_up/2
        self.jump_force = -270

        # Health Component
        self.health = Health(self, 3)
        self.health.height *= 1.5
        self.health.offset += 10

        # Weapon
        self.ammo = 4
        self.capacity = self.ammo
        self.projectiles = []
        for i in range(self.ammo):
            kunai = Kunai(f'Kunai_{i}', self)
            self.projectiles.append(kunai)
            Settings.GAMEOBJECTS.update({kunai.name: kunai})

        self.prompt = 'Ammo Prompt'
        UI.canvas.update({self.prompt: UI(self.prompt, 100, 100)})

        # Animations
        self.animator = Animator()

        self.IDLE = 'Idle'
        self.RUN = 'Run'
        self.JUMP_UP = 'JumpU'
        self.JUMP_DOWN = 'JumpD'
        self.THROW = 'Throw'
        self.DEAD = 'Dead'

        add = self.animator.add_animation
        add(self.IDLE, Animation((77, 146)))
        add(self.RUN, Animation((110, 146)))
        add(self.JUMP_UP, Animation((110, 170)))
        add(self.JUMP_DOWN, Animation((110, 170)))
        add(self.THROW, Animation((130, 150)))
        add(self.DEAD, Animation((160, 166)))

        get = self.animator.animations.get
        get(self.JUMP_UP).loop = False
        get(self.JUMP_DOWN).loop = False
        get(self.DEAD).loop = False

        load = pygame.image.load
        for i in range(10):
            get(self.IDLE).sprites.append(load(f'../images/object1/Idle/Idle__00{i}.png'))
            get(self.RUN).sprites.append(load(f'../images/object1/Run/Run__00{i}.png'))
            get(self.THROW).sprites.append(load(f'../images/object1/Throw/Throw__00{i}.png'))
            get(self.DEAD).sprites.append(load(f'../images/object1/Dead/Dead__00{i}.png'))

            if i < 5:
                get(self.JUMP_UP).sprites.append(load(f'../images/object1/Jump/Jump__00{i}.png'))
            else:
                get(self.JUMP_DOWN).sprites.append(load(f'../images/object1/Jump/Jump__00{i}.png'))

        for animation in self.animator.animations.values():
            animation.resize()

        # Flags
        self.state = self.IDLE
        self.jumping = False
        self.old_y = None
        self.going_down = False

    def update(self):
        super().update()
        self.controls()
        self.animation()

        UI.canvas.get(self.prompt).change_surface(f'X {self.ammo}')
        self.health.update()

    def controls(self):
        not_dead = not self.state == self.DEAD
        keys = []
        if not_dead:
            # Get Input
            keys = pygame.key.get_pressed()

            # THROW
            if keys[self.THROW_KEY] and not self.jumping and not self.state == self.THROW and self.ammo > 0:
                self.get_kunai().throw()
                return

            if self.state == self.THROW:
                if self.animator.get_current_counter(self.THROW) < self.animator.get_last_counter(self.THROW):
                    return

            # JUMP
            elif keys[self.JUMP_KEY] and not self.state == self.THROW and not self.jumping:
                self.jumping = True

        if self.jumping:
            self.do_jump()

        if not_dead:
            # RUN
            if keys[self.LEFT_KEY] or keys[self.RIGHT_KEY]:
                if keys[self.LEFT_KEY] and self.west_boundary():
                    self.x -= self.speed
                    self.flip = True
                if keys[self.RIGHT_KEY] and self.east_boundary():
                    self.x += self.speed
                    self.flip = False

                self.state = self.RUN
                return

            self.state = self.IDLE

    def animation(self):

        if self.jumping:
            if self.going_down:
                self.animator.animate(self.JUMP_DOWN, self)
            else:
                self.animator.animate(self.JUMP_UP, self)
        else:
            self.animator.animate(self.state, self)

    def do_jump(self):
        if self.old_y is None:
            self.old_y = copy.deepcopy(self.y)

        target = self.old_y + self.jump_force

        if self.old_y + self.jump_force < Settings.OFFSET:
            target = Settings.OFFSET

        if self.y > target and not self.going_down:
            self.y -= self.jump_speed_up
            return

        self.going_down = True

        if self.y < self.old_y:
            self.y += self.jump_speed_down
        else:
            if not self.y == self.old_y:
                self.y = self.old_y

            self.old_y = None
            self.going_down = self.jumping = False

    def get_kunai(self) -> Kunai:
        for ammo in self.projectiles:
            if not ammo.active:
                self.ammo -= 1
                self.state = self.THROW
                return ammo

    def dead(self):
        self.health.decrease_hp(1)

        if self.health.get_hp() <= 0:
            self.state = self.DEAD

            if Settings.RUNNING:
                Settings.DEATH_SOUND.play()

            Settings.MESSAGE = Settings.LOSE
            Settings.RUNNING = False

    def reset(self):
        self.ammo = self.capacity
        self.state = self.IDLE
        self.x = Settings.WIDTH/2
        self.old_y = None
        self.going_down = self.jumping = False
        self.y = 600
        self.health.reset()

        for proj in self.projectiles:
            proj.active = False
            proj.last_shown = None
