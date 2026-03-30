import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Custom Event Example")

clock = pygame.time.Clock()

sprite1 = pygame.Rect(150, 200, 60, 60)
sprite2 = pygame.Rect(400, 200, 60, 60)

color1 = (255, 0, 0)
color2 = (0, 0, 255)

CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CHANGE_COLOR:
            color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)

    pygame.display.update()
    clock.tick(60)