# No tutorial sheets are referenced for this 
import pygame

clock = pygame.time.Clock()

window_dimensions = (500, 500)
fps = 60 # frames per second
dt = 1/fps # duration of each frame

window = pygame.display.set_mode(window_dimensions)

# constants
gravity = 50 # pixels per s^2
restitution = 0.99 # how much velocity is conserved on collision

# initializing ball's position and velocity
position = pygame.Vector2(0,250)
velocity = pygame.Vector2(100,0)
radius = 10

# updating physics per frame
def update():
    # this ensures our function can write
    # to position and velocity
    global position, velocity

    # euler integration
    position += velocity * dt
    velocity.y += gravity * dt

    # collision detection
    if position.x < radius:
        velocity.x *= -restitution
        position.x = radius
    elif position.x > window_dimensions[0]-radius:
        velocity.x *= -restitution
        position.x = window_dimensions[0]-radius 
    
    # collision detectiongit
    if position.y < radius:
        velocity.y *= -restitution
        position.y = radius
    elif position.y > window_dimensions[1]-radius:
        velocity.y *= -restitution
        position.y = window_dimensions[1]-radius 
    

running = True
while running:
    window.fill((20,20,20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 

    # updating the physics before drawing
    # the next frame:
    update()

    pygame.draw.circle(window, (200,0,0), position, radius)

    pygame.display.update()
    
    clock.tick(fps)

