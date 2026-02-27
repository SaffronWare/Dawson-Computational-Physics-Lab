import pygame

pygame.init()

FPS = 60 # number of frames a second
dt = 1/FPS # time between each frame

WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dawson Simulation Lab")

clock = pygame.time.Clock()

# Particle 1
p1_y = 200
v1_y = 0

# Particle 2
p2_y = 300
v2_y = 0

mass = 1
k = 50       # spring stiffness
rest_length = 50
damping = 2

gravity = 500      # pixels per second^2
floor_y = 350
radius = 15

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    distance = p2_y - p1_y
    displacement = distance - rest_length

    force = -k * displacement

    
    a1 = -force / mass
    a2 = +force / mass

    a1 -= damping * v1_y
    a2 -= damping * v2_y

    v1_y += a1 * dt
    v2_y += a2 * dt

    v1_y += gravity * dt
    v2_y += gravity * dt

    p1_y += v1_y * dt
    p2_y += v2_y * dt


    
    if p1_y > floor_y:
        p1_y = floor_y
        v1_y *= -0.8

    
    if p2_y > floor_y:
        p2_y = floor_y
        v2_y *= -0.8

    window.fill((0, 0, 0))

    
    pygame.draw.circle(window, (0, 255, 0), (300, int(p1_y)), 10)
    pygame.draw.circle(window, (0, 255, 0), (300, int(p2_y)), 10)

    pygame.draw.line(window, (255, 255, 255),
                     (300, int(p1_y)),
                     (300, int(p2_y)), 2)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()