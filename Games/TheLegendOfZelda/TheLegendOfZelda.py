import pygame
import sys

pygame.init

screen = pygame.display.set_mode((800, 600))

class Actor:
    def __init__(self, x, y, images):
        self.images = {direction: pygame.image.load(image_path) for direction, image_path in images.items()}
        self.image = self.images['down']  # Default image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change

    def change_direction_and_size(self, direction, width, height):
        if direction in self.images:
            self.image = pygame.transform.scale(self.images[direction], (width, height))
            self.rect = self.image.get_rect(topleft=self.rect.topleft)

images = {
    'up': 'c:/Users/alvin/code/python/Games/TheLegendOfZelda/LinkBehind.png',
    'down': 'c:/Users/alvin/code/python/Games/TheLegendOfZelda/LinkFront.png',
    'left': 'c:/Users/alvin/code/python/Games/TheLegendOfZelda/LinkSide2.png',
    'right': 'c:/Users/alvin/code/python/Games/TheLegendOfZelda/LinkSide1.png'
}

titleScreen = pygame.image.load("Games/TheLegendOfZelda/FrontPage.png")
titleScreen = pygame.transform.scale(titleScreen, (800, 600))
screen.blit(titleScreen, (0, 0))
pygame.display.flip()
keyPressed = False
while not keyPressed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Check if the 's' key is pressed
                keyPressed = True

link = Actor(400, 300, images)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        link.move(-5, 0)
        link.change_direction_and_size('left', 90, 90)
    if keys[pygame.K_RIGHT]:
        link.move(5, 0)
        link.change_direction_and_size('right', 90, 90)
    if keys[pygame.K_UP]:
        link.move(0, -5)
        link.change_direction_and_size('up', 90, 90)
    if keys[pygame.K_DOWN]:
        link.move(0, 5)
        link.change_direction_and_size('down', 90, 90)
    
    screen.fill((255, 255, 255))

    link.draw(screen)

    pygame.display.flip()

    pygame.time.Clock().tick(60)