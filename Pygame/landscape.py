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

# Functions

# Used to find gradient colors by finding the difference of the start and end RGB (one of them) values and dividing them by the number of steps 
# to get the number needed to increment each step and then multiply by the current step for when it's not the first step.
def gradient_calc(start:int ,end:int, step_number:int, current_step:int):
    return round(((start - end) / step_number) * current_step) 
    
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
sun_angle = 180
moon_x = 0
moon_y = 0
moon_angle = 0

frames_passed = 0

day_sky_color = (135, 206, 255)
day_cloud_color = (240, 240 , 240)

night_sky_color = (15 , 20 , 45)
night_cloud_color = ( 80 , 90 , 110)

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

    # Moving the Sun
    
    # Increment angle
    sun_angle += 0.015
    
    # Convert to radians because sin and cos need radians for some reason
    sun_radians = math.radians(sun_angle)
    
    # Finding out the coordinates for the next sun (300 and 275 make sure that the sun goes in a big circle)
    sun_x = 320 + int(300 * math.cos(sun_angle))
    
    sun_y = 350 + int(275 * math.sin(sun_angle))

    # Moving the Moon
    
    # Convert to radians because sin and cos need radians for some reason
    moon_radians = math.radians(moon_angle)
    
    # Make angle 180 degrees (pi) from the sun
    moon_angle = sun_angle + math.pi
    
    # Finding out the coordinates for the next sun (300 and 275 make sure that the sun goes in a big circle)
    moon_x = 320 + int(300 * math.cos(moon_angle))
        
    moon_y = 350 + int(275 * math.sin(moon_angle))    

    # We use a sin function for the oscillating effect (going up and down), and then we add one so that the max and min is not -1 and 1, but 0 and 2. 
    # Then, we divide by 2 to make the max 0 and 1. Lastly, we multiply by 100 to make it a range from 0 to 100.
    gradient_step = int(((math.sin(sun_angle) + 1) / 2) * 100)

    # Subtracts gradient_calc's result from the R,G or B value of the sky or cloud color during the day.
    sky_r = day_sky_color[0] - gradient_calc(day_sky_color[0] , night_sky_color[0] , 100 , gradient_step)
    sky_g = day_sky_color[1] - gradient_calc(day_sky_color[1] , night_sky_color[1] , 100 , gradient_step)
    sky_b = day_sky_color[2] - gradient_calc(day_sky_color[2] , night_sky_color[2] , 100 , gradient_step)

    cloud_r = day_cloud_color[0] - gradient_calc(day_cloud_color[0] , night_cloud_color[0] , 100 , gradient_step)
    cloud_g = day_cloud_color[1] - gradient_calc(day_cloud_color[1] , night_cloud_color[1] , 100 , gradient_step)
    cloud_b = day_cloud_color[2] - gradient_calc(day_cloud_color[2] , night_cloud_color[2] , 100 , gradient_step)

    sky_color = (sky_r, sky_g, sky_b)
    cloud_color = (cloud_r, cloud_g , cloud_b)

    
    # DRAWING
    screen.fill((sky_color))  # always the first drawing command 
    
    # Drawing the Sun
    sun_color = (252,245,95)
    pygame.draw.circle(screen , sun_color , (sun_x ,sun_y), 60)
    
    # Drawing the Moon
    moon_color = (246,241,243)
    pygame.draw.circle(screen , moon_color , (moon_x , moon_y), 60)

    # Sapling
    sapling_bark_color = ( 111 , 78 , 55 )
    sapling_leaves_color = ( 34 , 139 , 34 )

    if frames_passed < 450: # Checks if less than 390 frames (15 seconds) have passed

        # Trunk
        pygame.draw.rect(screen , sapling_bark_color , (WIDTH // 2 , 310 , 10 , 70))

        # Leaves
        pygame.draw.polygon(screen , sapling_leaves_color , (sapling_leaf_right))
        pygame.draw.polygon(screen , sapling_leaves_color , (sapling_leaf_left))

    # Tree (Fully grown)

    if frames_passed >= 450: # Checks if 390 frames (15 seconds) or more have passed
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
    n = 40
    while n < WIDTH:
        y = HEIGHT - 40 + math.sin(n) * 30
        pygame.draw.rect(screen, (65, 140 , 35), (n, y, 3, 30))
        n += 10

    # Fence

    # Vertical part 
    i = 30
    while i <= WIDTH -30:
        y = 385
        pygame.draw.rect(screen, (255, 255, 255), (i, y, 10, 45))
        i += 30

    # Horizontal part
    pygame.draw.rect(screen, (255, 255 , 255), (30 , 400 , WIDTH -60 , 10 ))
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    frames_passed += 1
    #---------------------------

pygame.quit()