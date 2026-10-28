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

cloud_1_x = 250
cloud_1_y = 72

cloud_2_x = 10
cloud_2_y = 120

cloud_3_x = 486
cloud_3_y = 162

sun_x = 0
sun_y = 0

frames_passed = 0

sapling_leaf_left = [(319 , 307) , (319 , 328) , (274, 301) , (287,289)]
sapling_leaf_right = [(331, 331) , (371,297) , (366,288) , (329,308)]
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #elif event.type == pygame.MOUSEBUTTONDOWN:
            #print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    #print(frames_passed)

    # Moving the cloud right
    cloud_1_x += 3
    cloud_2_x += 3
    cloud_3_x += 3

    # Moving clouds back when they go too far to the right
    if cloud_1_x >= WIDTH + 40:
        cloud_1_x = -102

    if cloud_2_x >= WIDTH + 40:
        cloud_2_x = -102

    if cloud_3_x >= WIDTH + 40:
        cloud_3_x = -102


    # DRAWING
    screen.fill((135, 206, 255))  # always the first drawing command

    # Sun
    sun_color = (252,245,95)
    pygame.draw.circle(screen ,sun_color , (sun_x ,sun_y), 60)

    # Tree (not grown)
    sapling_bark_color = ( 111 , 78 , 55 )
    sapling_leaves_color = ( 34 , 139 , 34 )

    if frames_passed < 300: # Checks if less than 300 frames (10 seconds) have passed

        # Trunk
        pygame.draw.rect(screen , sapling_bark_color , (WIDTH // 2 , 310 , 10 , 70))

        # Leaves
        pygame.draw.polygon(screen , sapling_leaves_color , (sapling_leaf_right))
        pygame.draw.polygon(screen , sapling_leaves_color , (sapling_leaf_left))

    # Tree (Fully grown)

    if frames_passed >= 300: # Checks if 300 frames (10 seconds) or more have passed
        tree_bark_color = ( 111 , 78 , 55 )
        tree_leaves_color = ( 34 , 139 , 34 )

        # Trunk
        pygame.draw.rect(screen , sapling_bark_color , (WIDTH // 2 - 10 , 270 , 40 , 130))

        # Leaves
        pygame.draw.circle(screen, tree_leaves_color , (284 , 247), 40)
        pygame.draw.circle(screen, tree_leaves_color , (287 , 192), 40)
        pygame.draw.circle(screen, tree_leaves_color , (340 , 170), 40)
        pygame.draw.circle(screen, tree_leaves_color , (379 , 200), 40)
        pygame.draw.circle(screen, tree_leaves_color , (385 , 236), 40)
        pygame.draw.circle(screen, tree_leaves_color , (330 , 241), 40)
        

    # Cloud 1
    cloud_color = (240,240,240)
    pygame.draw.circle(screen, cloud_color , (cloud_1_x , cloud_1_y), 40)
    pygame.draw.circle(screen, cloud_color , (cloud_1_x + 46 , cloud_1_y + 15), 40)
    pygame.draw.circle(screen, cloud_color , (cloud_1_x - 15 , cloud_1_y + 20), 40)

    # Cloud 2
    pygame.draw.circle(screen, cloud_color , (cloud_2_x , cloud_2_y), 40)
    pygame.draw.circle(screen, cloud_color , (cloud_2_x + 33 , cloud_2_y + 25), 40)
    pygame.draw.circle(screen, cloud_color , (cloud_2_x - 20 , cloud_2_y + 30), 40)

    # Cloud 3
    pygame.draw.circle(screen, cloud_color , (cloud_3_x , cloud_3_y), 40)
    pygame.draw.circle(screen, cloud_color , (cloud_3_x + 33 , cloud_3_y + 25), 40)
    pygame.draw.circle(screen, cloud_color , (cloud_3_x - 20 , cloud_3_y + 30), 40)

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
    frames_passed += 1
    #---------------------------


pygame.quit()