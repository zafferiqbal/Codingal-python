import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Game Screen")

clock = pygame.time.Clock()

player = pygame.Rect(100, 200, 50, 50)
enemy = pygame.Rect(400, 200, 50, 50)

player_color = (0, 255, 0)
enemy_color = (255, 0, 0)

speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, player_color, player)
    pygame.draw.rect(screen, enemy_color, enemy)

    pygame.display.update()
    clock.tick(60)