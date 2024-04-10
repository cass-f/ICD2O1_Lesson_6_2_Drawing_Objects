import pygame

#Importang math for the arc
import math

# Initialize the game engine
pygame.init()

# ---------------------------
# Set window settings (size and name) 
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Racecar")
# ---------------------------

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

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

    #                                       Sky
    screen.fill((3, 107, 156)) 

    #-----------------------------------------------------------------------------

    #                           Front of car (infront of cockpit)
    pygame.draw.polygon(screen, (100, 0, 0), [[600, 357], [670, 357], [600, 322]])
    pygame.draw.line(screen, (50, 0, 0), [669, 359], [600, 359], 5)
    pygame.draw.polygon(screen, (100, 0, 0), [[410, 307], [410, 287], [550, 307]])

    #-----------------------------------------------------------------------------

    #                                   Cockpit
    pygame.draw.line(screen, (100, 0, 0), [550, 340], [200, 340], 65)
    pygame.draw.line(screen, (50, 0, 0), [550, 362], [200, 362], 5)
    pygame.draw.polygon(screen, (100, 0, 0), [[410, 307], [410, 287], [400, 307]])
    pygame.draw.polygon(screen, (100, 0, 0), [[320, 307], [320, 295], [400, 307]])

    #-----------------------------------------------------------------------------

    #                            Back of car (behind cockpit)

    #Headrest behind cockpit
    pygame.draw.line(screen, (100, 0, 0), [290, 300], [330, 300], 20)
    pygame.draw.rect(screen, (100, 0, 0), [290, 245 ,40 ,60 ])
    pygame.draw.rect(screen, (50, 0, 0), [290, 255 ,40 ,32 ])
    
    #Slope down from headrest
    pygame.draw.polygon(screen, (100, 0, 0), [[180, 287], [290, 245], [290, 287]])
    pygame.draw.polygon(screen, (50, 0, 0), [[200, 287], [290, 255], [290, 287]])
    pygame.draw.rect(screen, (100, 0, 0), [180, 287 ,120 ,60 ])

    #-----------------------------------------------------------------------------

    #                                  Lower body
    pygame.draw.line(screen, (100, 0, 0), [137, 340], [550, 340], 65)
    pygame.draw.line(screen, (50, 0, 0), [137, 362], [550, 362], 5)

    #-----------------------------------------------------------------------------

    #                                   Spoiler
    pygame.draw.rect(screen, (100, 0, 0), [100, 292 ,125 ,40 ])
    pygame.draw.polygon(screen, (100, 0, 0), [[125, 360], [100, 337], [120, 337]])
    pygame.draw.rect(screen, (100, 0, 0), [100, 297 ,125 ,40 ])
    pygame.draw.polygon(screen, (100, 0, 0), [[135, 260], [155, 260], [165, 292], [145, 292]])
    pygame.draw.rect(screen, (0, 0, 0), [120, 260 ,45 ,10 ])
    pygame.draw.polygon(screen, (0, 0, 0), [[165, 270], [145, 280], [145, 270]])
    pygame.draw.rect(screen, (0, 0, 0), [120, 265 ,25 ,16 ])

    #-----------------------------------------------------------------------------

    #                               Front Wheel
    pygame.draw.circle(screen, (0, 0, 0), [560, 347], 50)
    pygame.draw.circle(screen, (125, 125, 125), [560, 347], 35)
    pygame.draw.circle(screen, (173, 173, 172), [560, 347], 25)
    pygame.draw.line(screen, (125, 125, 125), [585, 347], [535, 347], 5)
    pygame.draw.line(screen, (125, 125, 125), [560, 372], [560, 322], 5)
    pygame.draw.circle(screen, (125, 125, 125), [560, 347], 10)

    #-----------------------------------------------------------------------------

    #                               Back Wheel
    pygame.draw.circle(screen, (0, 0, 0), [170, 347], 50)
    pygame.draw.circle(screen, (125, 125, 125), [170, 347], 35)
    pygame.draw.circle(screen, (173, 173, 172), [170, 347], 25)
    pygame.draw.line(screen, (125, 125, 125), [195, 347], [145, 347], 5)
    pygame.draw.line(screen, (125, 125, 125), [170, 372], [170, 322], 5)
    pygame.draw.circle(screen, (125, 125, 125), [170, 347], 10)

    #-----------------------------------------------------------------------------

    #                             Addition detail 307 400
    pygame.draw.rect(screen, (50, 0, 0), [390, 315 ,10 ,30])
    pygame.draw.rect(screen, (255, 255, 255), [275, 317 ,110 ,2])
    pygame.draw.rect(screen, (255, 255, 255), [275,321 ,110 ,2])
    pygame.draw.rect(screen, (255, 255, 255), [275, 325 ,110 ,2])
    pygame.draw.rect(screen, (255, 255, 255), [275, 340 ,110 ,2])
    pygame.draw.rect(screen, (50, 0, 0), [260, 315 ,10 ,30])

    #-----------------------------------------------------------------------------

    #                                Background Details

    #Bridge
    pygame.draw.rect(screen, (125, 125, 125), [0, 387 ,800 ,30 ])
    pygame.draw.arc(screen, (125, 125, 125), [-23, 407, 300, 445], math.pi/2, math.pi/5,10) 
    pygame.draw.arc(screen, (125, 125, 125), [0, 407, 300, 445], math.pi/5, math.pi/2,10) 
    pygame.draw.arc(screen, (125, 125, 125), [230, 407, 300, 445], math.pi/2, math.pi/5,10) 
    pygame.draw.arc(screen, (125, 125, 125), [253, 407, 300, 445], math.pi/5, math.pi/2,10) 
    pygame.draw.arc(screen, (125, 125, 125), [483, 407, 300, 445], math.pi/2, math.pi/5,10) 
    pygame.draw.arc(screen, (125, 125, 125), [506, 407, 300, 445], math.pi/5, math.pi/2,10) 

    #Clouds
    pygame.draw.circle(screen, (255, 255, 255), [70, 108], 40)
    pygame.draw.circle(screen, (255, 255, 255), [100, 75], 30)
    pygame.draw.circle(screen, (255, 255, 255), [150, 65], 50)
    pygame.draw.circle(screen, (255, 255, 255), [200, 108], 40)
    pygame.draw.rect(screen, (255, 255, 255), [70, 100 ,130 ,48])

    pygame.draw.circle(screen, (255, 255, 255), [370, 158], 50)
    pygame.draw.circle(screen, (255, 255, 255), [400, 125], 40)
    pygame.draw.circle(screen, (255, 255, 255), [450, 115], 60)
    pygame.draw.circle(screen, (255, 255, 255), [520, 163], 45)
    pygame.draw.rect(screen, (255, 255, 255), [370, 150 ,150 ,58])

    #Sun
    pygame.draw.circle(screen, (245, 191, 15), [700, 0], 100)
    
    #-----------------------------------------------------------------------------

    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
