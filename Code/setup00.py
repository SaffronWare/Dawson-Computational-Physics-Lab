# No reference sheets are avaible for this file
# library we are going to use for rendering
import pygame

# useful later on for keeping track of fps
clock = pygame.time.Clock()

# window size
window_dimensions = (500, 500)
fps = 60 # frames per second
dt = 1/fps # duration of each frame

# creating a window
window = pygame.display.set_mode(window_dimensions)

# This variable will tell us when to stop our main loop
running = True
while running:
    # recoloring window background
    window.fill((20,20,20))

    # going through all of the user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 

    # drawing a circle
    #-----------------surface----color------x---y--radius-
    pygame.draw.circle(window, (200,0,0), (250,250), 10)

    # displaying the new window
    pygame.display.update()
    
    # ensuring our framerate is capped
    clock.tick(fps)

