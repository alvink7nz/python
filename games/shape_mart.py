import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Mart Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
COLOURS = (BLACK, GREEN, BLUE, YELLOW, CYAN, MAGENTA)

# Define actor properties
actor_radius = 50
actor_thickness = 2
actor_x = WIDTH // 2
actor_y = HEIGHT // 2
actor_speed = 5

# Define target properties
target_radius = 15
target_x = WIDTH // 3
target_y = HEIGHT // 3

# Define green circle properties
green_circle_radius = 100
green_circle_x = WIDTH // 3 * 2
green_circle_y = HEIGHT // 3 * 2

customer_x, customer_y = 300, 10

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        actor_x -= actor_speed
    if keys[pygame.K_RIGHT]:
        actor_x += actor_speed
    if keys[pygame.K_UP]:
        actor_y -= actor_speed
    if keys[pygame.K_DOWN]:
        actor_y += actor_speed
    
    targetIsInActor = False
    # Ensure actor stays within the circle boundaries
    distance = math.sqrt((actor_x - WIDTH//2)**2 + (actor_y - HEIGHT//2)**2)
    if distance > (HEIGHT//2 - actor_radius):
        angle = math.atan2(actor_y - HEIGHT//2, actor_x - WIDTH//2)
        actor_x = WIDTH//2 + (HEIGHT//2 - actor_radius) * math.cos(angle)
        actor_y = HEIGHT//2 + (HEIGHT//2 - actor_radius) * math.sin(angle)

    # Check if the actor touches the target
    distance_to_target_circle = math.sqrt((actor_x - target_x)**2 + (actor_y - target_y)**2)
    if distance_to_target_circle < actor_radius + target_radius:
        # Move the target to the center of the green circle
        target_x, target_y = actor_x, actor_y
        targetIsInActor = True
    
    # Check if the actor touches the green circle
    distance_to_green_circle = math.sqrt((actor_x - green_circle_x)**2 + (actor_y - green_circle_y)**2)
    if distance_to_green_circle < actor_radius + green_circle_radius and target_x == actor_x:
        # Move the target into the green circle
        target_x, target_y = green_circle_x, green_circle_y
        targetIsInActor = False

    triangle_vertices = [(WIDTH // 2, 0), (WIDTH // 4, HEIGHT // 2), (3 * WIDTH // 4, HEIGHT // 2)]
    scaled_triangle_vertices = [(v[0] // 4, v[1] // 4) for v in triangle_vertices]
    customer_colour = random.choice(COLOURS)
    # Draw the green circle
    pygame.draw.circle(screen, GREEN, (green_circle_x, green_circle_y), green_circle_radius)

    # Draw the target (small circle)
    pygame.draw.circle(screen, RED, (int(target_x), int(target_y)), target_radius)

    # Draw the square actor (hollow circle)
    pygame.draw.circle(screen, BLACK, (int(actor_x), int(actor_y)), actor_radius, actor_thickness)

    pygame.draw.polygon(screen, customer_colour, scaled_triangle_vertices)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()