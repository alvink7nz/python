from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

selectedBlock = "dirt.png"
app = Ursina(title="minecraft")
player = FirstPersonController(
    mouse_sensesivity=Vec2(100, 100),
    position=(0, 5, 0),
    speed=5
)
blockTextures = {
    "grass": load_texture("alvin/python/grass.png"),
    "dirt": load_texture("alvin/python/dirt.png"),
    "stone": load_texture("alvin/python/stone.png"),
    "bedrock": load_texture("alvin/python/bedrock.png")
}
def Block(position, blocktype):
    texture_path = blocktype
    texture = load_texture(texture_path)
    return Entity(model="cube", position=position, scale=1, origin_y=-0.5, texture=texture, collider="box")



for i in range(-10, 10):
    for j in range(-10, 10):
        Block((i, 0, j), "grass.png")

def input(key):
    if key == "left mouse down":
        hit_info = raycast(camera.world_position, camera.forward, distance=10)
        if hit_info.hit:
            block = Block(hit_info.entity.position + hit_info.normal, selectedBlock)
    if key == "right mouse down" and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

Sky()
app.run()