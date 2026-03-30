import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

background_color = (0, 0, 0)
rect_color = (0, 128, 255)

font = pygame.font.SysFont(None, 36)
text = font.render("Hello Pygame", True, (255, 255, 255))
text_rect = text.get_rect(center=(320, 100))

rect = pygame.Rect(0, 0, 200, 100)
rect.center = (320, 240)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color)
    pygame.draw.rect(screen, rect_color, rect)
    screen.blit(text, text_rect)
    pygame.display.update()