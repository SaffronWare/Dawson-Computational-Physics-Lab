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
    def __init__(self, position=None, velocity=None, radius=2, mass=1, color=(255,255,255)):
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


class Spring:
    # Our spring will connect two points with a spring of strength k.
    def __init__(self, strength : float, p1 : Particle, p2 : Particle):
        # Damping is useful to make sure our springs dont oscilate permanently
        self.damping = 0.99
        self.k = strength
        self.p1 = p1
        self.p2 = p2 

        # Needed rest_length to compute delta_x in spring equation F = -k *delta_x
        self.rest_length = (p1.position - p2.position).length()

        # If we want to create rigid bodies, we can convert the springs into rigid
        # rods, this variable will be used to enable/disable that.
        self.rigid = False

    def apply_spring(self):
        # to avoid the program exploding, before we do anything we check that the particles aren't
        # too close
        if (self.p2.position - self.p1.position).length_squared() <= 0.05:
            return

        if self.rigid:
            # rigid rod case
            
            #1. Compute current length
            length = (self.p2.position - self.p1.position).length()

            #2. Compute delta_length (amount the poits have to move to reach rest_lenth)
            delta_length = length - self.rest_length

            #3. Compute amount p1 and p2 should move.
            ratio_p1 = self.p2.mass/(self.p1.mass + self.p2.mass)
            ratio_p2 = 1 - ratio_p1

            d1 = delta_length * ratio_p1 * self.k # for rigid springs, k will be how fast it corrects distances
            d2 = delta_length * ratio_p2 * self.k

            #4. Compute direction to move
            move_direction = (self.p2.position - self.p1.position).normalize()

            #5. Move each by the amount
            self.p1.position += d1 * move_direction
            self.p2.position += d2 * move_direction

            #6. Update the velocities
            # since we moved by some distance in one frame, the velocity also along the
            # direction of movement should be d1/dt and d2/dt for p1 and p2 respectively

            # first we eliminate the current component of velocity in that direction
            self.p1.velocity = self.p1.velocity - self.p1.velocity.dot(move_direction) * move_direction * self.k
            self.p2.velocity = self.p2.velocity - self.p2.velocity.dot(move_direction) * move_direction * self.k

            # finally we set the component of velocity in that direction to d/dt
            self.p1.velocity += d1 * move_direction / dt 
            self.p2.velocity += d2 * move_direction / dt

            
        else:
            # non rigid rod case
            #1. Compute current length
            length = (self.p2.position - self.p1.position).length()

            #2. Compute delta_x or delta_length since we are in 2D springs.
            delta_length = length - self.rest_length

            #3. Compute spring force
            spring_force = self.k * delta_length
            
            #4. Compute direction (normalized) the force will be applied in
            force_direction = (self.p2.position - self.p1.position).normalize()

            #4+ Damping
            damping = (self.p2.velocity - self.p1.velocity).dot(force_direction) * self.damping

            #5. Update particle velocities
            self.p1.velocity += (spring_force+damping) * force_direction / self.p1.mass * dt
            self.p2.velocity -= (spring_force+damping) * force_direction / self.p2.mass * dt
        
    def draw(self):
        if self.rigid:
            pygame.draw.line(window, (255,255,255), self.p1.position, self.p2.position, 4)
        else:
            pygame.draw.line(window, (160,160,160), self.p1.position, self.p2.position, 2)


"""-----------------CREATING VARIABLES ------------------------------------------------"""     






particles = [Particle(Vector2(250,250)), Particle(Vector2(300,300)), Particle(Vector2(250,300)), Particle(Vector2(300,250))]
springs = [Spring(100,particles[0], particles[1]), 
           Spring(100,particles[1], particles[2]), 
           Spring(100, particles[0], particles[2]),
           Spring(100, particles[0], particles[3]),
           Spring(100,particles[1],particles[3]),
           Spring(100,particles[2],particles[3])]

springs[1].rigid = False
springs[2].rigid = False




"--------------------END VARIABLES SECTION----------------------"





# collision check function

def colliding(particle1, particle2):
    # compute distance
    d = (particle2.position - particle1.position).length_squared()

    # return if they are colliding
    return d <= (particle1.radius + particle2.radius)**2

def respondCollision(particle1, particle2):
    # compute normal
    normal = particle2.position - particle1.position

    collision_loss = 0.5

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
        particle1.velocity = v1 +  alpha * normal
        particle2.velocity = v2 + beta * normal
        particle1.velocity -= collision_loss * particle1.velocity.dot(normal) * normal
        particle2.velocity -= collision_loss * particle2.velocity.dot(normal) * normal

# updating physics per frame
def update():
    # this ensures our function has access to particles, gravity and dt variables
    global window, particles, gravity, dt, springs

    # we loop through all our particles
    for particle in particles:
        # update each particle
        particle.update()

    for spring in springs:
        spring.apply_spring()
    
    for _ in range(5):
        for spring in springs:
            if spring.rigid:
                spring.apply_spring()

    # check for collisions
    for i in range(len(particles)):
        for j in range(i+1, len(particles)):
            if colliding(particles[i], particles[j]):
                respondCollision(particles[i], particles[j])


def draw():

    for spring in springs:
        spring.draw()

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

