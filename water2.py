import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Water Simulation")

# Set up the wave parameters
amplitude = 20
period = 20
frequency = 0.1
phase = 0

# Set up the water surface
water_surface = pygame.Surface((width, height))
water_surface.set_alpha(128)

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the waves
    for x in range(width):
        y = height / 2 + amplitude * math.sin(2 * math.pi * x / period - frequency * phase)
        pygame.draw.line(water_surface, (0, 0, 255), (x, y), (x, height))

    # Update the phase
    phase += 1

    # Draw the water surface
    screen.blit(water_surface, (0, 0))

    # Update the display
    pygame.display.update()
