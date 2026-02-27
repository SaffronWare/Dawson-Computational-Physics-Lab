# 00 — Setting Up Pygame

---
This will allow us to create a window where we can draw our objects

## 1. Install Pygame

Install pygame on the terminal by running:

pip install pygame

---

## 2. Basic Template

```python
import pygame

pygame.init()

FPS = 60 # number of frames a second
dt = 1/FPS # time between each frame

WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dawson Simulation Lab")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clears the window
    window.fill((0, 0, 0))

    # drawing a circle (we'll use this later on to draw our particles)
    pygame.draw.circle(window, (255, 0, 0), (300, 200), 20)
    #                  window   color        position, radius

    # refreshes the window
    pygame.display.flip()

    # ensures proper delay between frames
    clock.tick(FPS)

pygame.quit()
```


