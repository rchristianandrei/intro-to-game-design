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
bg_music = pygame.mixer.Sound('../music/suspense.mp3')
Settings.DEATH_SOUND = pygame.mixer.Sound('../music/death.mp3')
Settings.HIT_SOUND = pygame.mixer.Sound('../music/stab.mp3')
Settings.BIRD_SOUND = pygame.mixer.Sound('../music/bird.mp3')
Settings.HP_SOUND = pygame.mixer.Sound('../music/hp_up.mp3')

Settings.HIT_SOUND.set_volume(Settings.VOLUME)
Settings.DEATH_SOUND.set_volume(Settings.VOLUME)
Settings.BIRD_SOUND.set_volume(Settings.VOLUME)
Settings.HP_SOUND.set_volume(Settings.VOLUME)
bg_music.set_volume(Settings.VOLUME)
bg_music.play(-1)

# Objects
ninja = Settings.player_name
Settings.GAMEOBJECTS.update({ninja: Ninja(ninja)})

# Game Manager
manager = GameManager()
buff_manager = BuffManager()
manager.check_if_win()

background_image = pygame.image.load('../images/bg2.png')
kunai_icon = pygame.transform.scale(pygame.image.load('../images/object1/Kunai/Kunai.png'), (32, 160))
icon_location = (20, 10)

score = 'Score'
UI.canvas.update({score: UI(score, Settings.WIDTH//2, Settings.HEIGHT//2)})
score_UI = UI.canvas.get(score)

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

    for obj in Settings.GAMEOBJECTS.values():
        if not obj.active:
            continue
        obj.update()
        window.blit(obj.animator.active_sprite, (obj.actual_x(), obj.actual_y()))

        if isinstance(obj, Enemy) or isinstance(obj, Ninja):
            pygame.draw.rect(window, obj.health.color, obj.health.rect)

    # UI
    for ui in UI.canvas.values():
        ui.update()
        window.blit(ui.rect, (ui.actual_x(), ui.actual_y()))
    window.blit(kunai_icon, icon_location)

    if not Settings.RUNNING:
        score_UI.change_surface(Settings.MESSAGE)

    # Game Manager
    manager.check_if_win()
    buff_manager.update()

    # Update counter for animation
    if Animator.counter < Animator.limit:
        Animator.counter += 1
    else:
        Animator.counter = 0

    pygame.display.update()

pygame.quit()
