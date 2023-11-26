from pygame import *

init()
screen = display.set_mode((800,600))
running = True
while running:
    square = image.load("alvin/python/pixilart-drawing.png")
    mySurface = Surface((800,600))
    mySurface.fill((0,0,128))
    image_rect = mySurface.get_rect()
    while True:
        for events in event.get():
            if events.type == KEYDOWN:
                if events.key == K_ESCAPE:
                    running = False
            if events.type == QUIT:
                    running = False
        screen.blit(mySurface, image_rect)
        print("done")
        display.flip()
quit()