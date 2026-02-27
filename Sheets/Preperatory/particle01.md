# 01 Creating a basic particle

------------------------------------------------------------------------

In this sheet, we will create a basic bouncing ball.
------------------------------------------------------------------------

1.

To track a particle’s motion, we need to know its velocity and position.

Insert this block of code before our main loop:
```
position_y = 200
velocity_y = 0

gravity = 500      # pixels per second^2
floor_y = 350
radius = 15
```

-   position_y tells us where the ball is.
-   velocity_y tells us how fast it is moving.
-   gravity is a constant acceleration pulling the ball downward.
-   floor_y is the vertical position of the ground.
-   radius is the size of the ball.

------------------------------------------------------------------------

2. Updating motion

Inside the main loop (before drawing), we now update velocity and
position.

We use something called Euler integration.

Velocity changes because of acceleration:
```

    velocity_y += gravity * dt

    position_y += velocity_y * dt
```

-   Gravity increases velocity every frame.
-   Velocity moves the ball.
-   dt makes the motion consistent across different computers.

Without dt, physics would depend on frame rate.

------------------------------------------------------------------------

3. Collision with the floor

Now we check if the ball hits the floor.

Add this after updating position:

```
    if position_y > floor_y:
        position_y = floor_y
        velocity_y *= -0.8
```
We multiply by -0.8 to flip direction and absorb some of the speed.

------------------------------------------------------------------------

4. Drawing the particle

Draw the particle using:

```
    pygame.draw.circle(window, (255, 0, 0), (300, int(position_y)), radius)
```

Now the ball falls and bounces.

------------------------------------------------------------------------

