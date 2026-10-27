# pygame template

import pygame
import math


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

cloud_x = 148
cloud_y = 72

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    cloud_x += 3

    if cloud_x >= WIDTH + 40:
        cloud_x = -102

    # DRAWING
    screen.fill((135, 206, 255))  # always the first drawing command

    # Cloud
    cloud_color = (240,240,240)
    pygame.draw.circle(screen, cloud_color , (cloud_x , cloud_y), 40)
    pygame.draw.circle(screen, cloud_color , (cloud_x + 46 , cloud_y + 25), 40)
    pygame.draw.circle(screen, cloud_color , (cloud_x - 15 , cloud_y + 40), 40)

    # Hill
    rect = (-50, HEIGHT -100, WIDTH + 100, HEIGHT // 2)
    pygame.draw.ellipse(screen , (92, 172 , 45) , rect)

    # Grass
    x = 40
    while x < WIDTH:
        y = HEIGHT - 40 + math.sin(x) * 30
        pygame.draw.rect(screen, (65, 140 , 35), (x, y, 3, 30))
        x += 10
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()