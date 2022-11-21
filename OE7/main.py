from enemySpawnManager import EnemySpawnManager
from interface import UI
from animator import Animator
from settings import Settings
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

Settings.HIT_SOUND.set_volume(0.05)
Settings.DEATH_SOUND.set_volume(0.05)
bg_music.set_volume(0.05)
bg_music.play(-1)


# Objects
ninja = 'Ninja_0'
Settings.GAMEOBJECTS.update({ninja: Ninja(ninja)})

spawner = EnemySpawnManager()

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

    # Reset
    if pygame.key.get_pressed()[pygame.K_r]:
        Settings.RUNNING = True
        Settings.TIME_ENDED = None
        Settings.SCORE = 0

        for obj in Settings.GAMEOBJECTS.values():
            if obj.tag == 'Enemy':
                obj.active = False

        Settings.TIME_Start = pygame.time.get_ticks() / 1000
        Settings.GAMEOBJECTS.get(ninja).reset()
        score_UI.change_surface('')
        UI.canvas.get('Kills').change_surface(f'Score {Settings.SCORE}')

    # Update game objects
    window.blit(background_image, (0, -300))

    for obj in Settings.GAMEOBJECTS.values():
        if not obj.active:
            continue
        obj.update()
        window.blit(obj.animator.active_sprite, (obj.actual_x(), obj.actual_y()))

        if isinstance(obj, Enemy) or isinstance(obj, Ninja):
            pygame.draw.rect(window, obj.health.color, obj.health.rect)

    spawner.update()

    # UI
    for ui in UI.canvas.values():
        ui.update()
        window.blit(ui.rect, (ui.actual_x(), ui.actual_y()))
    window.blit(kunai_icon, icon_location)

    if not Settings.RUNNING:
        if Settings.TIME_ENDED is None:
            Settings.TIME_ENDED = int(round(pygame.time.get_ticks() / 1000 - Settings.TIME_Start))

            seconds = Settings.TIME_ENDED % 60
            minutes = int((Settings.TIME_ENDED - seconds) / 60)

            Settings.TIME_ENDED = 'You survived for '
            if minutes == 0:
                Settings.TIME_ENDED += f'{seconds} seconds!'
            else:
                Settings.TIME_ENDED += f'{minutes} : {seconds} minutes!'

            score_UI.change_surface(Settings.TIME_ENDED)

    # Update counter for animation
    if Animator.counter < Animator.limit:
        Animator.counter += 1
    else:
        Animator.counter = 0

    pygame.display.update()

pygame.quit()
