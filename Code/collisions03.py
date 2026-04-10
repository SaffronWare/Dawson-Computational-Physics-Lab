import pygame
from pygame import Vector2 
from random import randint as r

clock = pygame.time.Clock()

window_dimensions = (500, 500)
fps = 600 # frames per second
dt = 1/fps # duration of each frame

window = pygame.display.set_mode(window_dimensions)

# constants
gravity = 50 # pixels per s^2
restitution = 0.99 # how much velocity is conserved on collision

# Our particle data structure
class Particle:
    # Function that creates a particle
    def __init__(self, position=None, velocity=None, radius=10, mass=1, color=(255,255,255)):
        # Next to the function argument, when we write =, we set a default value
        # Example : radius=5 means radius will be put as 5 if the user doesnt input anything for the radius
        if position is None:
            position = Vector2()
        
        if velocity is None:
            velocity = Vector2()

        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.color = color 

        # added a mass variable
        self.mass = self.radius**2

    # function to update our particle
    def update(self):
        self.velocity.y += gravity * dt
        self.position += self.velocity * dt
        
        if self.position.x < self.radius:
            self.velocity.x *= -restitution
            self.position.x = self.radius
        elif self.position.x > window_dimensions[0]-self.radius:
            self.velocity.x *= -restitution
            self.position.x = window_dimensions[0]-self.radius 
        
        # collision detection
        if self.position.y < self.radius:
            self.velocity.y *= -restitution
            self.position.y = self.radius
        elif self.position.y > window_dimensions[1]-self.radius:
            self.velocity.y *= -restitution
            self.position.y = window_dimensions[1]-self.radius 

    # function to draw our particle
    def draw(self):
        pygame.draw.circle(window, self.color, self.position, self.radius)

"""
particles = [Particle(
    Vector2(r(0,window_dimensions[0]), r(0,window_dimensions[1])), 
    Vector2(r(-100,100), r(-100,100)),
    color=(r(0,255),r(0,255),r(0,255))
    ) 
    for i in range(10)]
"""

particles = [Particle(Vector2(window_dimensions[0]//2, 0), None, 50),Particle(Vector2(window_dimensions[0]//2, 150), None, 5),Particle(Vector2(window_dimensions[0]//2, 300), None, 40)]

# collision check function

def colliding(particle1, particle2):
    # compute distance
    d = (particle2.position - particle1.position).length_squared()

    # return if they are colliding
    return d <= (particle1.radius + particle2.radius)**2

def respondCollision(particle1, particle2):
    # compute normal
    normal = particle2.position - particle1.position

    # If there is a division by 0, we pass on collision to next frame
    if normal.length() >= 0.1:
        normal /= normal.length() # sets length to 1

        # compute alpha
        m1 = particle1.mass
        m2 = particle2.mass
        v1 = particle1.velocity
        v2 = particle2.velocity
        alpha = 2 * m2 / (m1 + m2) * (v2 - v1).dot(normal)

        # compute beta
        beta = -m1 * alpha / m2

        # update v1 and v2
        particle1.velocity = v1 + alpha * normal
        particle2.velocity = v2 + beta * normal

# updating physics per frame
def update():
    # this ensures our function has access to particles, gravity and dt variables
    global window, particles, gravity, dt 

    # we loop through all our particles
    for particle in particles:
        # update each particle
        particle.update()

    # check for collisions
    for i in range(len(particles)):
        for j in range(i+1, len(particles)):
            if colliding(particles[i], particles[j]):
                respondCollision(particles[i], particles[j])


def draw():
    for particle in particles:
        particle.draw()
    
    
running = True
while running:
    window.fill((20,20,20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 

    # updating all particles physics
    update()

    # drawing all particles
    draw()


    pygame.display.update()
    
    clock.tick(fps)

