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

triangle_width = 50
triangle_height = 50
triangle_color = MAGENTA
triangle_x = 0
triangle_y = 0
triangle_speed = 3

square_size = 100
square_x = 10  # Start from the left edge
square_y = 300  # Start from the top edge

font = pygame.font.SysFont(None, 36)

# Define the money
ownedMoney = 0
show_triangle = False

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
    if distance_to_green_circle < actor_radius + green_circle_radius:
        if target_x == actor_x:
            # Move the target into the green circle
            target_x, target_y = green_circle_x, green_circle_y
            targetIsInActor = False

    angle = math.atan2(target_y - triangle_y, target_x - triangle_x)
    dx = math.cos(angle) * triangle_speed
    dy = math.sin(angle) * triangle_speed

    # Move the triangle towards the target
    if (target_x == green_circle_x) and (target_y == green_circle_y):
        show_triangle =  True
        if show_triangle:
            triangle_x += dx
            triangle_y += dy

    # Draw the green circle
    pygame.draw.circle(screen, GREEN, (green_circle_x, green_circle_y), green_circle_radius)

    # Draw the target (small circle)
    pygame.draw.circle(screen, RED, (int(target_x), int(target_y)), target_radius)

    # Draw the circle actor (hollow circle)
    pygame.draw.circle(screen, BLACK, (int(actor_x), int(actor_y)), actor_radius, actor_thickness)

    pygame.draw.rect(screen, CYAN, (square_x, square_y, square_size, square_size))

    if show_triangle:
        pygame.draw.polygon(screen, triangle_color, [
        (triangle_x, triangle_y - triangle_height // 2),
        (triangle_x - triangle_width // 2, triangle_y + triangle_height // 2),
        (triangle_x + triangle_width // 2, triangle_y + triangle_height // 2)
    ])

    rect_width = 200
    rect_height = 100
    rect_x = 20
    rect_y = 20
    pygame.draw.rect(screen, GREEN, (rect_x, rect_y, rect_width, rect_height))

    # Render the variable number text
    text_surface = font.render(str(ownedMoney), True, BLACK)
    text_rect = text_surface.get_rect(center=(rect_x + rect_width // 2, rect_y + rect_height // 2))
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()