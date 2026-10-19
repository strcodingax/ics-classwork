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

circle_x = 200
circle_y = 200

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    # Color can be done in Hexadecimal, RGB, or words in quotations ("")
    # quotations only support basic colors (red, blue, green, etc.)
    
    screen.fill((255, 255, 255))  # always the first drawing command

    pygame.draw.rect(screen , (53 , 94 , 59) , (200,100,150,50))

    # for a rectangle, it's (surface, color (Hexadecimal, RGB, or words in quotations (""),
    # and then the x , y , width, and height in a tuple (bracket) ))

    pygame.draw.circle(screen, "blue", (350,150), 40)

    # for circles, it's (surface, color, center point, and radius)

    # bigger x and y values mean they move further down (y) or right (x).

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()