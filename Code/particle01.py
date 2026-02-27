import pygame

pygame.init()

FPS = 60 # number of frames a second
dt = 1/FPS # time between each frame

WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dawson Simulation Lab")

clock = pygame.time.Clock()


position_y = 200
velocity_y = 0

gravity = 500      # pixels per second^2
floor_y = 350
radius = 15

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    velocity_y += gravity * dt
    position_y += velocity_y * dt

    
    if position_y > floor_y:
        position_y = floor_y
        velocity_y *= -0.8

    window.fill((0, 0, 0))

    pygame.draw.circle(window, (255, 0, 0), (300, int(position_y)), radius)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()