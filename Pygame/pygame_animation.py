# pygame template

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = WIDTH // 2
circle_y = 50
circle_radius = 30
circle_speed_x = 20
circle_speed_y = 20
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    circle_speed_x *= 0.98
    circle_speed_y *= 0.98

    # Right wall check
    if circle_x >= WIDTH - circle_radius:
        circle_speed_x = -circle_speed_x

    # Left wall check
    elif circle_x <= 0 + circle_radius:
        circle_speed_x = -circle_speed_x

    # Bottom wall check
    elif circle_y >= HEIGHT - circle_radius:
        circle_speed_y = -circle_speed_y

    # Top wall check
    elif circle_y <= 0 + circle_radius:
        circle_speed_y = -circle_speed_y

    circle_x += circle_speed_x
    circle_y += circle_speed_y

   
    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), circle_radius)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()