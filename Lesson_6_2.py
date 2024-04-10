import pygame

# Initialize the game engine
pygame.init()

# ---------------------------
# Set window settings (size and name) 
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT) 

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("My game")
# ---------------------------

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
#Text
#variable = pygame.font.SysFont('Font name', font size, bold[true or false], italics[true or false])
#text = variable.render('Text', Anti-alising[true or false], RGB values)
    #Alising makes the font more clear and less pixel lated
    #REMEMBER! screen.blit(text, [300, 100]) is needed under the drawing section
font = pygame.font.SysFont('Arial', 25, True, False)
text = font.render('Welcome to my Game', True, (0, 0, 0))

# ---------------------------

# --------------- Main program loop ---------------
running = True
while running:
    # ----- EVENT HANDLING -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ----- GAME STATE UPDATES -----
    # All game math and comparisons happen here

    # ----- DRAWING -----
    screen.fill((255, 255, 255))  # always the first drawing command

    #Line
    #Skeleton: pygame.draw.line(location, RGB values, start point [x, y], end point [x, y], thickness)
    pygame.draw.line(screen, (122, 224, 212), [1, 1], [500, 100], 5)

    #Rectangle
    #Skeleton: pygame.draw.rect(location, RGB values, [x, y of top left corner value, width, height], thickness)
    pygame.draw.rect(screen, (127, 123, 120), [1, 1, 500, 100], 10)

    #Ellipse
    #Skeleton: pygame.draw.ellipse(location, RGB values, [x, y of top left corner value of ractangle, width, height], thickness)
        #It draws an imaginary rectangle and puts the ellipse within the rectangle
    pygame.draw.ellipse(screen, (12, 129, 124), [11, 11, 250, 79], 3)

    #Circle
    #Skeleton: pygame.draw.circle(location, RGB values, center of cirlce [x, y], radius, thickness)
    pygame.draw.circle(screen, (123, 120, 103), [400, 350], 75)

    #Arc (pi is needed, import math)
    #Skeleton: pygame.draw.arc(location. RGB values, rectangle boundaries [x, y, width, height], start angle, end angle, thickness)
    import math
    pygame.draw.arc(screen, (100, 0, 0), [400, 300, 300, 300], math.pi/5, math.pi/2,10) 

    #Polygon
    #Skeleton: pygame.draw.polygon(location, RGB values, [vertex 1 x, y], [vertex 2 x, y] [vertex 3 x, y], thickness)
        #You can have as many vertecies as you want
    pygame.draw.polygon(screen, (100, 0, 0), [[100, 280], [70, 250], [100, 250]], 5)

    #Text
    #screen.blit(text, [top left corner x, y])
        #REMEMBER! Rest of code under "Initialzing global variables"
    screen.blit(text, [300, 100])

    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
