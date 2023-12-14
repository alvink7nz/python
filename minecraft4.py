from minecraft import *
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
class Mob(Entity):
    def __init__(self, position=(0, 0, 0), scale=1, texture="slime.png"):
        super().__init__(
            model="cube",
            texture=texture,
            collider="box",
            scale=scale,
            position=position,
        )
mobs = []
def create_mobs(num_mobs=5):
    for _ in range(num_mobs):
        mob_position = (random.uniform(-10, 10), 1, random.uniform(-10, 10))
        mob = Mob(position=mob_position, scale=1)
        mobs.append(mob)
def create_tree(position, trunk_height=5, leaves_height=3):
    # Create trunk
    for k in range(trunk_height):
        Entity(model="cube", position=position, scale=1, origin_y=-0.5, texture="wood.png", collider="box")
    # Create leaves
    leaves_radius = 2
    for i in range(-leaves_radius, leaves_radius + 1):
        for j in range(-leaves_radius, leaves_radius + 1):
            for k in range(1, leaves_height + 1):
                if i**2 + j**2 + (k - 1)**2 <= leaves_radius**2:
                    Entity(model="cube", position=position, scale=1, origin_y=-0.5, texture="leaf.png", collider="box")
def create_mini_drop(position, block_type):
    # Create a mini drop entity at the given position
    mini_drop = Entity(model='cube', position=position, scale=0.5, collider='box', texture=block_type)
    mini_drops.append(mini_drop)

mini_drops = []
create_mobs()
treeSeed = random.uniform(0, 0.05)
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
                Entity(model="cube", position=(i, k - min_height, j), scale=1, origin_y=-0.5, texture="bedrock.png", collider="box")
            elif k == height:
                Entity(model="cube", position=(i, k - min_height, j), scale=1, origin_y=-0.5, texture="grass.png", collider="box")
                if random.random() < treeSeed:
                    create_tree(position=(i, k - min_height + 1, j), trunk_height=treeTrunk,leaves_height=treeLeaves)
            elif k > 2:
                Entity(model="cube", position=(i, k - min_height, j), scale=1, origin_y=-0.5, texture="dirt.png", collider="box")
            else:
                Entity(model="cube", position=(i, k - min_height, j), scale=1, origin_y=-0.5, texture="stone.png", collider="box")
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
        hit_info = raycast(camera.world_position, camera.forward, distance=3)
        if hit_info.hit:
            Entity(model="cube", position=hit_info.entity.position + hit_info.normal, scale=1, origin_y=-0.5, texture=selectedBlock, collider="box")
    if key == "right mouse down" and mouse.hovered_entity:
        # Check if the player is clicking on a block
        if mouse.hovered_entity.texture:
            block_type = mouse.hovered_entity.texture

            # Store the position before destroying the block
            block_position = mouse.hovered_entity.position

            # Destroy the block
            destroy(mouse.hovered_entity)

            # Create a mini drop at the stored position
            create_mini_drop(block_position, block_type)


def update():
    global mini_drops

    # Iterate over mini drops in reverse order to avoid issues with modifying the list during iteration
    for mini_drop in reversed(mini_drops):
        # Check if the player is close enough to collect the mini drop
        if distance(player.position, mini_drop.position) < 2.5:
            # Collect the mini drop
            mini_drops.remove(mini_drop)
            destroy(mini_drop)
    for mob in mobs:
        mob.x += 1 * time.dt
Sky()
app.run()