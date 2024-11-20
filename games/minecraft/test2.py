from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()

ground = Entity(model="plane", scale=500, parent=scene, texture="grass.png", position=(0, -1, 0), collider="mesh")

ground.texture_scale = (500, 500)

def update():
    if held_keys["alt"]:
        player.speed = 10
    else:
        player.speed = 5

sky = Sky()

app.run()