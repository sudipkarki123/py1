import pygame
import sys
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame a2.py")
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
character = pygame.image.load("messi.jpg")
character = pygame.transform.scale(character, (100, 150))
font = pygame.font.Font(None, 50)
text = font.render("Hello World!", True, WHITE)
character_x = 100
character_y = 100
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x, character_y))
    screen.blit(text, (200, 200))
    pygame.display.flip()
pygame.quit()
sys.exit()


        
