from pygame import *
from pygame.locals import *
init()
screen = display.set_mode()
running = True
while running:
    for event in event.get:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == QUIT:
            running = False

quit()
                
