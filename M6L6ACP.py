import pygame
import sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Game with Background and Sound")

clock = pygame.time.Clock()

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (640, 480))

pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)

sprite1 = pygame.Rect(150, 200, 60, 60)
sprite2 = pygame.Rect(400, 200, 60, 60)

color1 = (255, 0, 0)
color2 = (0, 0, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)

    pygame.display.update()
    clock.tick(60)