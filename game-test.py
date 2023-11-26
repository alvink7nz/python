from pygame import *
from pygame.locals import *
init()
screen = display.set_mode((800,600))
running = True
while running:
    for events in event.get():
        if events.type == KEYDOWN:
            if events.key == K_ESCAPE:
                running = False
        if events.type == QUIT:
            running = False
quit()