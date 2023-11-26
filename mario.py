from pygame import *
from pygame.locals import *
import keyboard
init()
running = True
width, height = 1000, 700
screen = display.set_mode((width, height))
screen.fill((135, 206, 250))
class Actor(sprite.Sprite):
    def __init__(self, x, y, imagePath, width, height):
        super().__init__()
        self.image = image.load(imagePath)
        self.image = transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 15
    def update(self):
        for events in event.get():
            if events.type == KEYDOWN:
                if events.key == K_LEFT:
                    self.rect.x -= self.speed
                elif events.key == K_RIGHT:
                    self.rect.x += self.speed
mario = Actor(imagePath="alvin/python/images/mario.png", x=width//2, y=height//2, width=120, height=180)
allSprites = sprite.Group()
allSprites.add(mario)
while running:
    while True:
        for events in event.get():
            if events.type == KEYDOWN:
                if events.key == K_ESCAPE:
                    running = False
            if events.type == QUIT:
                    running = False
        screen.fill((135, 206, 250))
        allSprites.draw(screen)
        allSprites.update()
        display.flip()
quit()