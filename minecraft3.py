from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=3, seed=random.randint(1, 1000))
treeX = random.randint(-10, 10)
treeZ = random.randint(-10, 10)
selectedBlock = "dirt.png"
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
def create_tree(position, trunk_height=5, leaves_height=3):
    # Create trunk
    for k in range(trunk_height):
        Block((position[0], position[1] + k, position[2]), "wood.png")

    # Create leaves
    leaves_radius = 2
    for i in range(-leaves_radius, leaves_radius + 1):
        for j in range(-leaves_radius, leaves_radius + 1):
            for k in range(1, leaves_height + 1):
                if i**2 + j**2 + (k - 1)**2 <= leaves_radius**2:
                    Block((position[0] + i, position[1] + trunk_height + k - 1, position[2] + j), "leaf.png")
treeSeed = random.randint(0, 4)
if treeSeed == 0:
    treeSeed = 0.005
elif treeSeed == 1:
    treeSeed = 0.01
elif treeSeed == 2:
    treeSeed = 0.02
elif treeSeed == 3:
    treeSeed = 0.03
elif treeSeed == 4:
    treeSeed = 0.05
treeLeaves = random.randint(1, 3)
if treeLeaves == 1:
    treeTrunk = 2
if treeLeaves == 2:
    treeTrunk = 3
if treeLeaves == 3:
    treeTrunk = 5
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
                if random.random() < treeSeed:
                    create_tree(position=(i, k - min_height + 1, j), trunk_height=treeTrunk,leaves_height=treeLeaves)
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
    if key == "5":
        selectedBlock = "wood.png"
    if key == "6":
        selectedBlock = "leaf.png"
    if key == "left mouse down":
        hit_info = raycast(camera.world_position, camera.forward, distance=10)
        if hit_info.hit:
            Block(hit_info.entity.position + hit_info.normal, selectedBlock)
    if key == "right mouse down" and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

Sky()
app.run()