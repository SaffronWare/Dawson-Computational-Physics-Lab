# 00 — Setting Up Pygame

## Goal
Create a minimal simulation window that runs at a fixed frame rate and draws a circle.

This is the foundation for all physics simulations in this lab.

---

## 1. Install Pygame

Make sure Python 3 is installed.

Install pygame:

pip install pygame

---

## 2. Minimal Simulation Template

```python
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dawson Simulation Lab")

clock = pygame.time.Clock()

running = True
while running:
    # Limit to 60 FPS and compute delta time
    dt = clock.tick(60) / 1000  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    # Draw a simple circle
    pygame.draw.circle(window, (255, 0, 0), (300, 200), 20)

    pygame.display.flip()

pygame.quit()
```
