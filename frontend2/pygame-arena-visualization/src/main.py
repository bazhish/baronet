import pygame
from arena import Arena
from player import Player

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platform Arena Visualization")

# Create arena and player
player = pygame.Rect(100, 500, 50, 50)  # x, y, width, height

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player and arena


    # Draw everything
    screen.fill((150, 150, 150))  # Clear screen with black
    screen.blit(screen, (0, 0))  # Draw arena background
    pygame.draw.rect(screen, (255, 0, 0), player)

    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()