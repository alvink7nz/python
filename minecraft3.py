from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

selectedBlock = "grass.png"
app = Ursina(title="minecraft")
player = FirstPersonController(
    mouse_sensesivity=Vec2(100, 100),
    position=(0, 5, 0),
    speed=5
)

def Block(position, blocktype):
    texture_path = blocktype
    texture = load_texture(texture_path)
    return Entity(model="cube", position=position, scale=1, origin_y=-0.5, texture=texture, collider="box")
miniBlocksBlock = load_texture(selectedBlock)

miniBlock = Entity(
    parent=camera,
    scale=0.2,
    texture=miniBlocksBlock,
    position=(0.35, 0.25, 0.5)
)

for i in range(-10, 10):
    for j in range(-10, 10):
        Block((i, 0, j), selectedBlock)

Sky()
app.run()