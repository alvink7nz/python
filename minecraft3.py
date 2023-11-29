from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=3, seed=random.randint(1, 1000))
treeX = random.randint(-10, 10)
treeY = random.randint(-10, 10)
tree = [treeX, treeY]
selectedBlock = "dirt.png"
app = Ursina(title="minecraft")
player = FirstPersonController(
    mouse_sensesivity=Vec2(100, 100),
    position=(0, 5, 0),
    speed=5
)

class worldType():
    pass
def Block(position, blocktype):
    texture_path = blocktype
    texture = load_texture(texture_path)
    return Entity(model="cube", position=position, scale=1, origin_y=-0.5, texture=texture, collider="box")


min_height = -5
for i in range(-10, 10):
    for j in range(-10, 10):
        height = noise([i * 0.02, j * 0.02])
        height = math.floor(height * 7.5)
        for k in range(height, min_height - 1, -1):
            if k == min_height:
                Block((i, k - min_height, j), "bedrock.png")
            elif k == height:
                Block((i, k - min_height, j), "grass.png")
            elif k > 2:
                Block((i, k - min_height, j), "stone.png")
            else:
                Block((i, k - min_height, j), "dirt.png")

def input(key):
    global selectedBlock
    if key == "1":
        selectedBlock = "grass.png"
    if key == "2":
        selectedBlock = "dirt.png"
    if key == "3":
        selectedBlock = "stone.png"
    if key == "4":
        selectedBlock = "bedrock.png"
    if key == "left mouse down":
        hit_info = raycast(camera.world_position, camera.forward, distance=10)
        if hit_info.hit:
            Block(hit_info.entity.position + hit_info.normal, selectedBlock)
    if key == "right mouse down" and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

Sky()
app.run()