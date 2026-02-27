# 02 Two Particles Connected by a Spring

------------------------------------------------------------------------

In this sheet, we will connect two particles using a spring.

This introduces force-based simulation using Hooke’s Law.

Instead of gravity-only motion, the particles will now influence each
other.

------------------------------------------------------------------------

1. What We Need

Each particle needs:

-   Position
-   Velocity
-   Acceleration (computed from forces)

Insert this before the main loop:
```
# Particle 1
p1_y = 200
v1_y = 0

# Particle 2
p2_y = 300
v2_y = 0

mass = 1
k = 50          # spring stiffness
rest_length = 100
damping = 2
```
------------------------------------------------------------------------

2. Understanding the Spring

Hooke’s Law:

$$F = -k(x - x0)$$

Where: - k is stiffness - x is current distance - x0 is rest length

If stretched → spring pulls back. If compressed → spring pushes outward.

------------------------------------------------------------------------

3. Computing the Spring Force

Inside the main loop (before updating positions):
```
    distance = p2_y - p1_y
    displacement = distance - rest_length

    force = -k * displacement
```
This force acts on both particles in opposite directions.

------------------------------------------------------------------------

4. Apply Forces to Each Particle
```
    a1 += force / mass
    a2 -= -force / mass

    a1 -= damping * v1_y
    a2 -= damping * v2_y
```
------------------------------------------------------------------------

5. Integrate Motion (Euler)
```
    v1_y += a1 * dt
    v2_y += a2 * dt

    p1_y += v1_y * dt
    p2_y += v2_y * dt
```
Now the particles oscillate around the rest length.

------------------------------------------------------------------------

6. Drawing

    pygame.draw.circle(window, (0, 255, 0), (300, int(p1_y)), 10)
    pygame.draw.circle(window, (0, 255, 0), (300, int(p2_y)), 10)

    pygame.draw.line(window, (255, 255, 255),
                     (300, int(p1_y)),
                     (300, int(p2_y)), 2)

------------------------------------------------------------------------

