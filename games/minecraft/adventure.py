import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("c:/Users/alvin/code/python/games/minecraft/startMap.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
WHITE = (255, 255, 255)

# Actor class
class Actor:
    def __init__(self, x, y, image_path, size=(130, 100)):
        self.image = pygame.image.load(image_path).convert_alpha()  # Load image and support transparency
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=(x, y))  # Position image in center of actor
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, dx, dy):
        # Update position by changing rect.x and rect.y
        self.rect.x += dx
        self.rect.y += dy

# Instantiate actor with an image
knight = Actor(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "c:/Users/alvin/code/python/games/minecraft/knight.jpg", (100, 130))

# Game loop
clock = pygame.time.Clock()
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement control
    keys = pygame.key.get_pressed()
    dx = dy = 0
    if keys[pygame.K_LEFT]:
        dx = -5
    if keys[pygame.K_RIGHT]:
        dx = 5
    if keys[pygame.K_UP]:
        dy = -5
    if keys[pygame.K_DOWN]:
        dy = 5

    # Move the actor
    knight.move(dx, dy)

    # Update screen
    screen.blit(background, (0, 0))
    knight.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
