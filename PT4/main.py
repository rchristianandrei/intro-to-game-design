from game_manager import GameManager
from animator import Animator
from settings import Settings
from buff import BuffManager
from interface import UI
from ninja import Ninja
from enemy import Enemy
import pygame


pygame.init()

window = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
clock = pygame.time.Clock()

UI.font = pygame.font.SysFont('arial', 50)

pygame.display.set_caption(Settings.TITLE)

# Sounds
sound = pygame.mixer.Sound

bg_music = sound('../music/suspense.mp3')
Settings.DEATH_SOUND = sound('../music/death.mp3')
Settings.HIT_SOUND = sound('../music/stab.mp3')
Settings.BIRD_SOUND = sound('../music/bird.mp3')
Settings.HP_SOUND = sound('../music/hp_up.mp3')
Settings.WALK_SOUND = sound('../music/walking-sfx.mp3')
Settings.JUMP_SOUND = sound('../music/jump-sfx.mp3')
Settings.WIN_SOUND = sound('../music/win-sfx.mp3')
Settings.LOSE_SOUND = sound('../music/lose-sfx.mp3')

Settings.HIT_SOUND.set_volume(Settings.VOLUME)
Settings.DEATH_SOUND.set_volume(Settings.VOLUME)
Settings.BIRD_SOUND.set_volume(Settings.VOLUME)
Settings.HP_SOUND.set_volume(Settings.VOLUME)
Settings.WALK_SOUND.set_volume(Settings.VOLUME + 0.2)
Settings.JUMP_SOUND.set_volume(Settings.VOLUME)
Settings.WIN_SOUND.set_volume(Settings.VOLUME + 0.2)
Settings.LOSE_SOUND.set_volume(Settings.VOLUME + 0.2)
bg_music.set_volume(Settings.VOLUME)
bg_music.play(-1)

# Objects
ninja = Settings.player_name
Settings.GAMEOBJECTS.update({ninja: Ninja(ninja)})

# Game Manager
manager = GameManager()
buff_manager = BuffManager()
manager.check_if_win()

load = pygame.image.load

background_image = load('../images/bg2.png')
kunai_icon = pygame.transform.scale(load('../images/object1/Kunai/Kunai.png'), (32, 160))
icon_location = (20, 10)

arrow_image = pygame.transform.scale(load('../images/arrow-down.png'), (75, 75))
arrow_duration = 3
arrow_mark = None

# UI
score = 'Score'

UI.canvas.update({score: UI(score, Settings.WIDTH//2, Settings.HEIGHT//2)})
score_UI = UI.canvas.get(score)

title = Settings.TITLE
UI.menu.update({title: UI(title, Settings.WIDTH//2, Settings.HEIGHT//3, title)})

instruction = Settings.INSTRUCTION
UI.menu.update({instruction: UI(title, Settings.WIDTH//2, Settings.HEIGHT//2, instruction)})


def menu(keys):
    # UI
    for ui in UI.menu.values():
        ui.update()
        window.blit(ui.rect, (ui.actual_x(), ui.actual_y()))

    if keys[pygame.K_p]:
        Settings.PLAYING = True

        for ui in UI.menu.values():
            ui.surface = ''


def main_gameplay():
    # Game objects
    for obj in Settings.GAMEOBJECTS.values():
        if not obj.active:
            continue
        obj.update()
        window.blit(obj.animator.active_sprite, (obj.actual_x(), obj.actual_y()))

        if isinstance(obj, Enemy) or isinstance(obj, Ninja):
            pygame.draw.rect(window, obj.health.color, obj.health.rect)

        if isinstance(obj, Ninja):
            global arrow_mark
            if arrow_mark is None:
                arrow_mark = pygame.time.get_ticks() / 1000

            if pygame.time.get_ticks() / 1000 - arrow_mark < arrow_duration:
                window.blit(arrow_image, (obj.actual_x(), obj.actual_y() - 150))

    # UI
    for ui in UI.canvas.values():
        ui.update()
        window.blit(ui.rect, (ui.actual_x(), ui.actual_y()))
    window.blit(kunai_icon, icon_location)

    # Game Manager
    manager.check_if_win()
    buff_manager.update()

    # Update counter for animation
    if Animator.counter < Animator.limit:
        Animator.counter += 1
    else:
        Animator.counter = 0


def post_gameplay(keys):
    global running

    score_UI.change_surface(Settings.MESSAGE)

    if keys[pygame.K_SPACE]:
        running = False


running = True
while running:
    # Set FPS
    clock.tick(Settings.FPS)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    window.blit(background_image, (0, -300))

    keys = pygame.key.get_pressed()

    if not Settings.PLAYING:
        menu(keys)
    else:
        main_gameplay()

        if not Settings.RUNNING:
            post_gameplay(keys)

    pygame.display.update()

pygame.quit()
