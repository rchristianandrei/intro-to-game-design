import pygame
from object import Object


def main():
    pygame.init()

    width, height = 800, 600

    Object.height = height
    Object.width = width

    window = pygame.display.set_mode((width, height))
    playing = True

    pygame.display.set_caption("First Pygame")

    # Clock
    clock = pygame.time.Clock()

    # Initialize Objects
    object1 = Object(415, 275)
    object1.idle_scale = (77, 146)
    object1.run_scale = (110, 146)
    object1.w = 77
    object1.h = 146

    # Assign Sprite Settings
    load = pygame.image.load
    object1.IDLE = [load('../images/object1/Idle/Idle__000.png'),
                    load('../images/object1/Idle/Idle__001.png'),
                    load('../images/object1/Idle/Idle__002.png'),
                    load('../images/object1/Idle/Idle__003.png'),
                    load('../images/object1/Idle/Idle__004.png'),
                    load('../images/object1/Idle/Idle__005.png'),
                    load('../images/object1/Idle/Idle__006.png'),
                    load('../images/object1/Idle/Idle__007.png'),
                    load('../images/object1/Idle/Idle__008.png'),
                    load('../images/object1/Idle/Idle__009.png')]
    object1.RUN = [load('../images/object1/Run/Run__000.png'),
                   load('../images/object1/Run/Run__001.png'),
                   load('../images/object1/Run/Run__002.png'),
                   load('../images/object1/Run/Run__003.png'),
                   load('../images/object1/Run/Run__004.png'),
                   load('../images/object1/Run/Run__005.png'),
                   load('../images/object1/Run/Run__006.png'),
                   load('../images/object1/Run/Run__007.png'),
                   load('../images/object1/Run/Run__008.png'),
                   load('../images/object1/Run/Run__009.png')]
    object1.resize_sprites()

    while playing:
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        keys = pygame.key.get_pressed()

        # Assign keys
        object1.moving = [
            keys[pygame.K_w],
            keys[pygame.K_s],
            keys[pygame.K_a],
            keys[pygame.K_d],
            keys[pygame.K_SPACE]
        ]

        # Move Objects
        object1.move()

        # Draw Objects
        window.blit(object1.active_sprite, (object1.x, object1.y, object1.w, object1.h))

        # Update
        pygame.display.update()
        clock.tick(60)
        Object.counter += 1
        if Object.counter > 999:
            Object.counter = 0

    pygame.quit()


main()
