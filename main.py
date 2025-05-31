import pygame
pygame.init()
Display = pygame.display.set_mode((300, 300))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print("A key was pressed")
pygame.quit()
